import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from collective.fundraising.core.testing import\
    COLLECTIVE_FUNDRAISING_CORE_INTEGRATION


class TestEmailAdapters(unittest.TestCase):

    layer = COLLECTIVE_FUNDRAISING_CORE_INTEGRATION
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        from plone.dexterity.fti import DexterityFTI

        # Make fundraising_campaign type providing campaign and settings behavior
        fti = DexterityFTI('campaign')
        self.portal.portal_types._setObject('campaign', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingSettings',
                         'collective.fundraising.core.behaviors.interfaces.IFundraisingCampaign',)

        # Make personal_page type providing the page and personal fundraiser behaviors
        fti = DexterityFTI('personal_page')
        self.portal.portal_types._setObject('personal_page', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingPage',
                         'collective.fundraising.core.behaviors.interfaces.IPersonalFundraiser')
                        
        # Make fundraising_campaign type combining campaign and page behaviors
        fti = DexterityFTI('combo_page')
        self.portal.portal_types._setObject('combo_page', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingCampaign',
                         'collective.fundraising.core.behaviors.interfaces.IFundraisingPage',)

        # Make donation type combining honorary/memorial, donor and donation behaviors
        fti = DexterityFTI('combo_donation')
        self.portal.portal_types._setObject('combo_donation', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IDedication',
                         'collective.fundraising.core.behaviors.interfaces.IDonor',
                         'collective.fundraising.core.behaviors.interfaces.IDonation',)

        # Get Manager role
        from plone.app.testing import setRoles
        from plone.app.testing import TEST_USER_ID
        setRoles(self.portal, TEST_USER_ID, ['Manager'])


        # Create a single campaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        self.portal.invokeFactory('campaign', 'test_campaign', title=u"Test Fundraising Campaign")
        self.campaign = IFundraisingCampaign(self.portal['test_campaign'])

        # Create a page inside the campaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser
        self.campaign.context.invokeFactory('personal_page', 'test_page', title=u"Test Personal Page")
        self.page = IFundraisingPage(self.campaign.context['test_page'])
        self.personal_fundraiser = IPersonalFundraiser(self.campaign.context['test_page'])

        # Set test campaign values
        self.campaign.goal = 1000
        self.campaign.total = 150.0
      
        # Set test page values 
        self.page.goal = 200
        self.page.total = 50.0

        # Create a combo donation providing donor, donation, and dedication
        self.page.context.invokeFactory('combo_donation', 'test_combo_donation', title=u"Test Combo Donation")

        # Get an instance of each behavior of the combo donation
        donation = self.page.context['test_combo_donation']
        from collective.fundraising.core.behaviors.interfaces import IDonor
        self.donor = IDonor(donation)
        from collective.fundraising.core.behaviors.interfaces import IDonation
        self.donation = IDonation(donation)
        from collective.fundraising.core.behaviors.interfaces import IDedication
        self.dedication = IDedication(donation)

        # Set donor values
        self.donor.first_name = u"John"
        self.donor.last_name = u"Doe"
        self.donor.email = u"collective.fundraising.core.test@mailinator.com"
       
        # Set donation values 
        self.donation.amount = 10.0

        # Set dedication values
        self.dedication.dedication_type = u"memorial"
        self.dedication.first_name = u"George"
        self.dedication.last_name = u"Washington"
        self.dedication.recipient_first_name = u"John"
        self.dedication.recipient_last_name = u"Adams"
    
    def test_donation_thank_you(self):
        """ Test that Thank You data can be adapted from IDonation behavior
        """
        from collective.fundraising.core.emails.interfaces import IThankYouData
        data = IThankYouData(self.donation)

        self.assertEquals(data.first_name, u"John")
        self.assertEquals(data.last_name, u"Doe")
        self.assertEquals(data.amount, 10.0)
        #FIXME: Implement these methods and tests
        #self.assertEquals(data.block_receipt, u"")
        #self.assertEquals(data.block_thank_you, u"")

        self._test_campaign_fields(data)
        
    def test_dedication(self):
        """ Test that Dedication data can be adapted from IDedication behavior
        """
        from collective.fundraising.core.emails.interfaces import IDedicationData
        data = IDedicationData(self.donation)

        self.assertEquals(data.first_name, u"John")
        self.assertEquals(data.last_name, u"Doe")
        self.assertEquals(data.amount, 10.0)
        self.assertEquals(data.dedication_type, u"memorial")
        self.assertEquals(data.dedication_first_name, u"George")
        self.assertEquals(data.dedication_last_name, u"Washington")
        self.assertEquals(data.recipient_first_name, u"John")
        self.assertEquals(data.recipient_last_name, u"Adams")
        #FIXME: Implement this method and test
        #self.assertEquals(data.block_message, u"")

        self._test_campaign_fields(data)
        
    def test_personal_fundraiser_created(self):
        """ Test that Personal Fundraiser Created data can be adapted from IPersonalFundraiser behavior
        """
        self.personal_fundraiser.first_name = u"Thomas"
        self.personal_fundraiser.last_name = u"Jefferson"
        self.personal_fundraiser.pf_goal = 500

        from collective.fundraising.core.emails.interfaces import IPersonalFundraiserCreatedData
        data = IPersonalFundraiserCreatedData(self.personal_fundraiser)

        self.assertEquals(data.fundraiser_first, u"Thomas")
        self.assertEquals(data.fundraiser_last, u"Jefferson")
        #FIXME: Implement this method and test
        #self.assertEquals(data.block_message, u"")

        self._test_campaign_fields(data)
        
    def _test_campaign_fields(self, data):
        campaign_url = self.portal.absolute_url() + "/test_campaign"
        page_url = campaign_url + "/test_page"

        self.assertEquals(data.campaign_name, u"Test Fundraising Campaign")
        self.assertEquals(data.campaign_url, campaign_url)
        self.assertEquals(data.campaign_image_url, campaign_url + "/@@images/image")
        self.assertEquals(data.campaign_header_image_url, campaign_url + "/@@images/header_image")
        self.assertEquals(data.campaign_goal, 1000)
        self.assertEquals(data.campaign_raised, 150.0)
        self.assertEquals(data.campaign_percent, 15)
        self.assertEquals(data.page_name, u"Test Personal Page")
        self.assertEquals(data.page_url, page_url)
        self.assertEquals(data.page_image_url, page_url + '/@@images/image')
        self.assertEquals(data.page_goal, 200)
        self.assertEquals(data.page_raised, 50.0)
        self.assertEquals(data.page_percent, 25)
