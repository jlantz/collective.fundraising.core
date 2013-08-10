import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from collective.fundraising.core.testing import\
    COLLECTIVE_FUNDRAISING_CORE_INTEGRATION

import datetime
from plone.app.textfield.value import RichTextValue
from plone.namedfile.file import NamedBlobImage
from plone.namedfile.tests.test_image import zptlogo

class TestInheritance(unittest.TestCase):

    layer = COLLECTIVE_FUNDRAISING_CORE_INTEGRATION
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        from plone.dexterity.fti import DexterityFTI

        ### Single behavior types

        # Make organization type providing organization behavior
        fti = DexterityFTI('organization')
        self.portal.portal_types._setObject('organization', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingOrganization',)

        # Make campaign type providing campaign behavior
        fti = DexterityFTI('campaign')
        self.portal.portal_types._setObject('campaign', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingCampaign',)

        # Make fundraising_page type providing page behavior
        fti = DexterityFTI('fundraising_page')
        self.portal.portal_types._setObject('fundraising_page', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingPage',)

        # Make personal type providing personal fundraiser behavior
        fti = DexterityFTI('personal')
        self.portal.portal_types._setObject('personal', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IPersonalFundraiser',)

        ### Combination behavior types

        # Make organization_campaign type providing organization and campaign behaviors
        fti = DexterityFTI('organization_campaign')
        self.portal.portal_types._setObject('organization_campaign', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingOrganization',
                         'collective.fundraising.core.behaviors.interfaces.IFundraisingCampaign')

        # Make organization_campaign_page type providing organization, campaign, and page behaviors
        fti = DexterityFTI('organization_campaign_page')
        self.portal.portal_types._setObject('organization_campaign_page', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingOrganization',
                         'collective.fundraising.core.behaviors.interfaces.IFundraisingCampaign',
                         'collective.fundraising.core.behaviors.interfaces.IFundraisingPage')

        # Make organization_campaign_page type providing organization, campaign, and personal fundraiser behaviors
        fti = DexterityFTI('organization_campaign_personal')
        self.portal.portal_types._setObject('organization_campaign_personal', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingOrganization',
                         'collective.fundraising.core.behaviors.interfaces.IFundraisingCampaign',
                         'collective.fundraising.core.behaviors.interfaces.IPersonalFundraiser')

        # Make organization_campaign_page_personal type providing organization, campaign, page, and personal fundraiser behaviors
        fti = DexterityFTI('organization_campaign_page_personal')
        self.portal.portal_types._setObject('organization_campaign_page_personal', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingOrganization',
                         'collective.fundraising.core.behaviors.interfaces.IFundraisingCampaign',
                         'collective.fundraising.core.behaviors.interfaces.IFundraisingPage',
                         'collective.fundraising.core.behaviors.interfaces.IPersonalFundraiser')

        # Make organization_campaign_personal_page type providing organization, campaign, personal fundraiser, and page behaviors
        fti = DexterityFTI('organization_campaign_personal_page')
        self.portal.portal_types._setObject('organization_campaign_personal_page', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingOrganization',
                         'collective.fundraising.core.behaviors.interfaces.IFundraisingCampaign',
                         'collective.fundraising.core.behaviors.interfaces.IPersonalFundraiser',
                         'collective.fundraising.core.behaviors.interfaces.IFundraisingPage')

        # Make campaign_page type providing campaign and page behaviors
        fti = DexterityFTI('campaign_page')
        self.portal.portal_types._setObject('campaign_page', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingCampaign',
                         'collective.fundraising.core.behaviors.interfaces.IFundraisingPage')

        # Make campaign_personal type providing campaign and personal fundraiser behaviors
        fti = DexterityFTI('campaign_personal')
        self.portal.portal_types._setObject('campaign_personal', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingCampaign',
                         'collective.fundraising.core.behaviors.interfaces.IPersonalFundraiser')

        # Make campaign_page_personal type providing campaign, page, and personal fundraiser behaviors
        fti = DexterityFTI('campaign_page_personal')
        self.portal.portal_types._setObject('campaign_page_personal', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingCampaign',
                         'collective.fundraising.core.behaviors.interfaces.IFundraisingPage',
                         'collective.fundraising.core.behaviors.interfaces.IPersonalFundraiser')

        # Make campaign_personal_page type providing campaign, personal fundraiser, and page behaviors
        fti = DexterityFTI('campaign_personal_page')
        self.portal.portal_types._setObject('campaign_personal_page', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingCampaign',
                         'collective.fundraising.core.behaviors.interfaces.IPersonalFundraiser',
                         'collective.fundraising.core.behaviors.interfaces.IFundraisingPage')

        # Make page_personal type providing page and personal fundraiser behaviors
        fti = DexterityFTI('page_personal')
        self.portal.portal_types._setObject('page_personal', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingPage',
                         'collective.fundraising.core.behaviors.interfaces.IPersonalFundraiser')

        # Make personal_page type providing personal fundraiser and page behaviors
        fti = DexterityFTI('personal_page')
        self.portal.portal_types._setObject('personal_page', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IPersonalFundraiser',
                         'collective.fundraising.core.behaviors.interfaces.IFundraisingPage')

        # Get Manager role
        from plone.app.testing import setRoles
        from plone.app.testing import TEST_USER_ID
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def check_inheritance(self, organization, campaign, page, personal, page_personal=None, personal_page=None):
        """ Check the inheritance logic against a set of behavior instances """

        # Build values which are not simple types for use later in the test
        organization_image = NamedBlobImage(zptlogo, filename=u'organization_image.gif')
        organization_thank_you = RichTextValue(u"Test Organization Thank You", 'text/plain', 'text/html')
        organization_pf_thank_you = RichTextValue(u"Test Organization Personal Thank You", 'text/plain', 'text/html')

        campaign_image = NamedBlobImage(zptlogo, filename=u'campaign_image.gif')
        campaign_thank_you = RichTextValue(u"Test Campaign Thank You", 'text/plain', 'text/html')
        campaign_pf_thank_you = RichTextValue(u"Test Campaign Personal Thank You", 'text/plain', 'text/html')
        campaign_date_start = datetime.date(2013,1,15)

        page_image = NamedBlobImage(zptlogo, filename=u'page_image.gif')
        page_date_start = datetime.date(2013,2,15)

        personal_image = NamedBlobImage(zptlogo, filename=u'personal_image.gif')
        personal_pf_thank_you = RichTextValue(u"Test Personal Fundraiser Thank You", 'text/plain', 'text/html')
        personal_date_start = datetime.date(2013,3,15)

        if page_personal:
            page_personal_image = NamedBlobImage(zptlogo, filename=u'page_personal_image.gif')
            page_personal_pf_thank_you = RichTextValue(u"Test Personal Fundraiser Page Thank You", 'text/plain', 'text/html')
            page_personal_date_start = datetime.date(2013,3,15)

        if personal_page:
            personal_page_image = NamedBlobImage(zptlogo, filename=u'personal_page_image.gif')
            personal_page_date_start = datetime.date(2013,2,15)

        # Check that all subobjects inherit from organization
        organization.goal = 1000
        organization.pf_goal = 100
        organization.image = organization_image
        organization.thank_you = organization_thank_you
        organization.pf_thank_you = organization_pf_thank_you

        self.assertEqual(organization.goal, 1000)
        self.assertEqual(organization.pf_goal, 100)
        self.assertEqual(organization.image.filename, organization_image.filename)
        self.assertEqual(organization.thank_you, organization_thank_you)
        self.assertEqual(organization.pf_thank_you, organization_pf_thank_you)

        self.assertEqual(campaign.goal, 1000)
        self.assertEqual(campaign.pf_goal, 100)
        self.assertEqual(campaign.image.filename, organization_image.filename)
        self.assertEqual(campaign.thank_you, organization_thank_you)
        self.assertEqual(campaign.pf_thank_you, organization_pf_thank_you)
        self.assertEqual(campaign.date_start, None)

        self.assertEqual(campaign.allow_pf, None)
        organization.allow_pf = True
        self.assertEqual(campaign.allow_pf, True)

        self.assertEqual(page.goal, 1000)
        self.assertEqual(page.pf_goal, 100)
        self.assertEqual(page.image.filename, organization_image.filename)
        self.assertEqual(page.date_start, None)

        self.assertEqual(personal.goal, 1000)
        self.assertEqual(personal.pf_goal, 100)
        self.assertEqual(personal.thank_you, organization_thank_you)
        self.assertEqual(personal.pf_thank_you, organization_pf_thank_you)
        self.assertEqual(personal.image.filename, organization_image.filename)
        self.assertEqual(personal.date_start, None)

        if page_personal is not None:
            self.assertEqual(page_personal.goal, 1000)
            self.assertEqual(page_personal.pf_goal, 100)
            self.assertEqual(page_personal.thank_you, organization_thank_you)
            self.assertEqual(page_personal.pf_thank_you, organization_pf_thank_you)
            self.assertEqual(page_personal.image.filename, organization_image.filename)
            self.assertEqual(page_personal.date_start, None)

        if personal_page is not None:
            self.assertEqual(personal_page.goal, 1000)
            self.assertEqual(personal_page.pf_goal, 100)
            self.assertEqual(personal_page.image.filename, organization_image.filename)
            self.assertEqual(personal_page.date_start, None)

        # Check that page and personal inherit from campaign
        campaign.goal = 2000
        campaign.pf_goal = 200
        campaign.image = campaign_image
        campaign.thank_you = campaign_thank_you
        campaign.pf_thank_you = campaign_pf_thank_you
        campaign.date_start = campaign_date_start
        campaign.allow_pf = False
        
        self.assertEqual(campaign.goal, 2000)
        self.assertEqual(campaign.pf_goal, 200)
        self.assertEqual(campaign.image.filename, campaign_image.filename)
        self.assertEqual(campaign.thank_you, campaign_thank_you)
        self.assertEqual(campaign.pf_thank_you, campaign_pf_thank_you)
        self.assertEqual(campaign.date_start, campaign_date_start)
        self.assertEqual(campaign.allow_pf, False)

        self.assertEqual(page.goal, 2000)
        self.assertEqual(page.pf_goal, 200)
        self.assertEqual(page.image.filename, campaign_image.filename)
        self.assertEqual(page.date_start, campaign_date_start)

        self.assertEqual(personal.goal, 2000)
        self.assertEqual(personal.pf_goal, 200)
        self.assertEqual(personal.image.filename, campaign_image.filename)
        self.assertEqual(personal.thank_you, campaign_thank_you)
        self.assertEqual(personal.pf_thank_you, campaign_pf_thank_you)
        self.assertEqual(personal.date_start, campaign_date_start)

        if page_personal is not None:
            self.assertEqual(page_personal.goal, 2000)
            self.assertEqual(page_personal.pf_goal, 200)
            self.assertEqual(page_personal.thank_you, campaign_thank_you)
            self.assertEqual(page_personal.pf_thank_you, campaign_pf_thank_you)
            self.assertEqual(page_personal.image.filename, campaign_image.filename)
            self.assertEqual(page_personal.date_start, campaign_date_start)

        if personal_page is not None:
            self.assertEqual(personal_page.goal, 2000)
            self.assertEqual(personal_page.pf_goal, 200)
            self.assertEqual(personal_page.image.filename, campaign_image.filename)
            self.assertEqual(personal_page.date_start, campaign_date_start)


        # Check that personal inherits from page if contained in page
        if page_personal is not None:
            page.goal = 3000
            page.pf_goal = 300
            page.image = page_image
            page.date_start = page_date_start

            self.assertEqual(page.goal, 3000)
            self.assertEqual(page.pf_goal, 300)
            self.assertEqual(page.image.filename, page_image.filename)
            self.assertEqual(page.date_start, page_date_start)

            self.assertEqual(page_personal.goal, 3000)
            self.assertEqual(page_personal.pf_goal, 300)
            self.assertEqual(page_personal.image.filename, page_image.filename)
            self.assertEqual(page_personal.date_start, page_date_start)

        # Check that page inherits from personal if contained in personal
        if personal_page is not None:
            personal.pf_goal = 400
            personal.image = personal_image
            personal.pf_thank_you = personal_pf_thank_you
            personal.date_start = personal_date_start

            self.assertEqual(personal.pf_goal, 400)
            self.assertEqual(personal.image.filename, personal_image.filename)
            self.assertEqual(personal.pf_thank_you, personal_pf_thank_you)
            self.assertEqual(personal.date_start, personal_date_start)

            self.assertEqual(personal_page.pf_goal, 400)
            self.assertEqual(personal_page.image.filename, personal_image.filename)
            self.assertEqual(personal_page.date_start, personal_date_start)



    def check_local_only(self, organization, campaign, page, personal, page_personal=None, personal_page=None):
        """ Check to insure that only local field values are returned for aggregate fields """

        # Ensure that campaign, page, and personal fundraiser aggregate fields do not inherit
        campaign.total = 100
        campaign.count = 1
        campaign.total_pledged = 200
        campaign.count_pledged = 2

        # All pages and personal fundraisers should have no value
        types = ['page','personal']
        if page_personal is not None:
            types.append('page_personal')
        if personal_page is not None:
            types.append('personal_page')
        for prefix in types:
            for field in ['total','count','total_pledged','count_pledged']:
                self.assertEqual(eval('%s.%s' % (prefix, field)), None)

        page.total = 300
        page.count = 3
        page.total_pledged = 400
        page.count_pledged = 4
        self.assertEqual(page.total, 300)
        self.assertEqual(page.count, 3)
        self.assertEqual(page.total_pledged, 400)
        self.assertEqual(page.count_pledged, 4)

        personal.total = 500
        personal.count = 5
        personal.total_pledged = 600
        personal.count_pledged = 6
        self.assertEqual(personal.total, 500)
        self.assertEqual(personal.count, 5)
        self.assertEqual(personal.total_pledged, 600)
        self.assertEqual(personal.count_pledged, 6)

        # All pages and personal fundraisers inside a page or personal fundraiser should have no value
        types = []
        if page_personal is not None:
            types.append('page_personal')
        if personal_page is not None:
            types.append('personal_page')
        for prefix in types:
            for field in ['total','count','total_pledged','count_pledged']:
                self.assertEqual(eval('%s.%s' % (prefix, field)), None)

        if page_personal is not None:
            page_personal.total = 700
            page_personal.count = 7
            page_personal.total_pledged = 800
            page_personal.count_pledged = 8
            self.assertEqual(page_personal.total, 700)
            self.assertEqual(page_personal.count, 7)
            self.assertEqual(page_personal.total_pledged, 800)
            self.assertEqual(page_personal.count_pledged, 8)

        if personal_page is not None:
            personal_page.total = 900
            personal_page.count = 9
            personal_page.total_pledged = 1000
            personal_page.count_pledged = 10
            self.assertEqual(personal_page.total, 900)
            self.assertEqual(personal_page.count, 9)
            self.assertEqual(personal_page.total_pledged, 1000)
            self.assertEqual(personal_page.count_pledged, 10)
        

    def test_single_behaviors(self):
        from collective.fundraising.core.behaviors.interfaces import IFundraisingOrganization
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

        self.portal.invokeFactory('organization', 'test_organization', title=u"Test Fundraising Organization")
        organization_obj = self.portal['test_organization']

        organization_obj.invokeFactory('campaign', 'test_campaign', title=u"Test Fundraising Campaign")
        campaign_obj = organization_obj['test_campaign']

        campaign_obj.invokeFactory('fundraising_page', 'test_page', title=u"Test Fundraising Page")
        page_obj = campaign_obj['test_page']

        page_obj.invokeFactory('personal', 'test_page_personal', title=u"Test Page Personal Fundraiser")
        page_personal_obj = page_obj['test_page_personal']

        campaign_obj.invokeFactory('personal', 'test_personal', title=u"Test Personal Fundraiser")
        personal_obj = campaign_obj['test_personal']

        personal_obj.invokeFactory('fundraising_page', 'test_personal_page', title=u"Test Personal Fundraiser Page")
        personal_page_obj = personal_obj['test_personal_page']

        organization = IFundraisingOrganization(organization_obj)
        campaign = IFundraisingCampaign(campaign_obj)
        page = IFundraisingPage(page_obj)
        page_personal = IPersonalFundraiser(page_personal_obj)
        personal = IPersonalFundraiser(personal_obj)
        personal_page = IFundraisingPage(personal_page_obj)

        self.check_inheritance(organization, campaign, page, personal, page_personal, personal_page)
        self.check_local_only(organization, campaign, page, personal, page_personal, personal_page)

    def test_combo_organization_campaign(self):
        from collective.fundraising.core.behaviors.interfaces import IFundraisingOrganization
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

        self.portal.invokeFactory('organization_campaign', 'test_organization_campaign', title=u"Test Fundraising Organization and Campaign")
        organization_campaign_obj = self.portal['test_organization_campaign']

        organization_campaign_obj.invokeFactory('fundraising_page', 'test_page', title=u"Test Fundraising Page")
        page_obj = organization_campaign_obj['test_page']

        page_obj.invokeFactory('personal', 'test_page_personal', title=u"Test Page Personal Fundraiser")
        page_personal_obj = page_obj['test_page_personal']

        organization_campaign_obj.invokeFactory('personal', 'test_personal', title=u"Test Personal Fundraiser")
        personal_obj = organization_campaign_obj['test_personal']

        personal_obj.invokeFactory('fundraising_page', 'test_personal_page', title=u"Test Personal Fundraiser Page")
        personal_page_obj = personal_obj['test_personal_page']

        organization = IFundraisingOrganization(organization_campaign_obj)
        campaign = IFundraisingCampaign(organization_campaign_obj)
        page = IFundraisingPage(page_obj)
        page_personal = IPersonalFundraiser(page_personal_obj)
        personal = IPersonalFundraiser(personal_obj)
        personal_page = IFundraisingPage(personal_page_obj)

        self.check_inheritance(organization, campaign, page, personal, page_personal, personal_page)
        self.check_local_only(organization, campaign, page, personal, page_personal, personal_page)

    def test_combo_organization_campaign_page(self):
        from collective.fundraising.core.behaviors.interfaces import IFundraisingOrganization
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

        self.portal.invokeFactory('organization_campaign_page', 'test_organization_campaign_page', title=u"Test Fundraising Organization, Campaign, and Page")
        organization_campaign_page_obj = self.portal['test_organization_campaign_page']

        organization_campaign_page_obj.invokeFactory('personal', 'test_personal', title=u"Test Personal Fundraiser")
        personal_obj = organization_campaign_page_obj['test_personal']

        personal_obj.invokeFactory('fundraising_page', 'test_personal_page', title=u"Test Personal Fundraiser Page")
        personal_page_obj = personal_obj['test_personal_page']

        organization = IFundraisingOrganization(organization_campaign_page_obj)
        campaign = IFundraisingCampaign(organization_campaign_page_obj)
        page = IFundraisingPage(organization_campaign_page_obj)
        personal = IPersonalFundraiser(personal_obj)
        personal_page = IFundraisingPage(personal_page_obj)

        self.check_inheritance(organization, campaign, page, personal, personal_page=personal_page)
        self.check_local_only(organization, campaign, page, personal, personal_page=personal_page)

    def test_combo_organization_campaign_personal(self):
        from collective.fundraising.core.behaviors.interfaces import IFundraisingOrganization
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

        self.portal.invokeFactory('organization_campaign_personal', 'test_organization_campaign_personal', title=u"Test Fundraising Organization, Campaign, and Personal Fundraiser")
        organization_campaign_personal_obj = self.portal['test_organization_campaign_personal']

        organization_campaign_personal_obj.invokeFactory('fundraising_page', 'test_page', title=u"Test Page")
        page_obj = organization_campaign_personal_obj['test_page']

        organization = IFundraisingOrganization(organization_campaign_personal_obj)
        campaign = IFundraisingCampaign(organization_campaign_personal_obj)
        page = IFundraisingPage(page_obj)
        personal = IPersonalFundraiser(organization_campaign_personal_obj)

        self.check_inheritance(organization, campaign, page, personal)
        self.check_local_only(organization, campaign, page, personal)

    def test_combo_organization_campaign_personal_page(self):
        from collective.fundraising.core.behaviors.interfaces import IFundraisingOrganization
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

        self.portal.invokeFactory('organization_campaign_personal_page', 'test_organization_campaign_personal_page', title=u"Test Fundraising Organization, Campaign, Personal Fundraiser, and Page")
        organization_campaign_personal_page_obj = self.portal['test_organization_campaign_personal_page']

        organization_campaign_personal_page_obj.invokeFactory('fundraising_page', 'test_page', title=u"Test Page")
        page_obj = organization_campaign_personal_page_obj['test_page']

        organization = IFundraisingOrganization(organization_campaign_personal_page_obj)
        campaign = IFundraisingCampaign(organization_campaign_personal_page_obj)
        page = IFundraisingPage(organization_campaign_personal_page_obj)
        personal = IPersonalFundraiser(organization_campaign_personal_page_obj)

        self.check_inheritance(organization, campaign, page, personal)
        self.check_local_only(organization, campaign, page, personal)

    def test_combo_organization_campaign_page_personal(self):
        from collective.fundraising.core.behaviors.interfaces import IFundraisingOrganization
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

        self.portal.invokeFactory('organization_campaign_page_personal', 'test_organization_campaign_page_personal', title=u"Test Fundraising Organization, Campaign, Page and Personal Fundraiser")
        organization_campaign_page_personal_obj = self.portal['test_organization_campaign_page_personal']

        organization_campaign_page_personal_obj.invokeFactory('fundraising_page', 'test_page', title=u"Test Page")
        page_obj = organization_campaign_page_personal_obj['test_page']

        organization = IFundraisingOrganization(organization_campaign_page_personal_obj)
        campaign = IFundraisingCampaign(organization_campaign_page_personal_obj)
        page = IFundraisingPage(organization_campaign_page_personal_obj)
        personal = IPersonalFundraiser(organization_campaign_page_personal_obj)

        self.check_inheritance(organization, campaign, page, personal)
        self.check_local_only(organization, campaign, page, personal)

    def test_combo_campaign_page_personal(self):
        from collective.fundraising.core.behaviors.interfaces import IFundraisingOrganization
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

        self.portal.invokeFactory('organization', 'test_organization', title=u"Test Fundraising Organization")
        organization_obj = self.portal['test_organization']

        organization_obj.invokeFactory('campaign_page_personal', 'test_campaign_page_personal', title=u"Test Fundraising Campaign, Page and Personal Fundraiser")
        campaign_page_personal_obj = organization_obj['test_campaign_page_personal']

        organization = IFundraisingOrganization(organization_obj)
        campaign = IFundraisingCampaign(campaign_page_personal_obj)
        page = IFundraisingPage(campaign_page_personal_obj)
        personal = IPersonalFundraiser(campaign_page_personal_obj)

        self.check_inheritance(organization, campaign, page, personal)
        self.check_local_only(organization, campaign, page, personal)

    def test_combo_campaign_personal_page(self):
        from collective.fundraising.core.behaviors.interfaces import IFundraisingOrganization
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

        self.portal.invokeFactory('organization', 'test_organization', title=u"Test Fundraising Organization")
        organization_obj = self.portal['test_organization']

        organization_obj.invokeFactory('campaign_personal_page', 'test_campaign_personal_page', title=u"Test Fundraising Campaign, Personal Fundraiser, and Page")
        campaign_personal_page_obj = organization_obj['test_campaign_personal_page']

        organization = IFundraisingOrganization(organization_obj)
        campaign = IFundraisingCampaign(campaign_personal_page_obj)
        page = IFundraisingPage(campaign_personal_page_obj)
        personal = IPersonalFundraiser(campaign_personal_page_obj)

        self.check_inheritance(organization, campaign, page, personal)
        self.check_local_only(organization, campaign, page, personal)

    def test_combo_campaign_page(self):
        from collective.fundraising.core.behaviors.interfaces import IFundraisingOrganization
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

        self.portal.invokeFactory('organization', 'test_organization', title=u"Test Fundraising Organization")
        organization_obj = self.portal['test_organization']

        organization_obj.invokeFactory('campaign_page', 'test_campaign_page', title=u"Test Fundraising Campaign and Page")
        campaign_page_obj = organization_obj['test_campaign_page']

        campaign_page_obj.invokeFactory('personal', 'test_personal', title=u"Test Personal Fundraiser")
        personal_obj = campaign_page_obj['test_personal']

        personal_obj.invokeFactory('fundraising_page', 'test_personal_page', title=u"Test Personal Fundraiser Page")
        personal_page_obj = personal_obj['test_personal_page']

        organization = IFundraisingOrganization(organization_obj)
        campaign = IFundraisingCampaign(campaign_page_obj)
        page = IFundraisingPage(campaign_page_obj)
        personal = IPersonalFundraiser(personal_obj)
        personal_page = IFundraisingPage(personal_page_obj)

        self.check_inheritance(organization, campaign, page, personal, personal_page=personal_page)
        self.check_local_only(organization, campaign, page, personal, personal_page=personal_page)

    def test_combo_campaign_personal(self):
        from collective.fundraising.core.behaviors.interfaces import IFundraisingOrganization
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

        self.portal.invokeFactory('organization', 'test_organization', title=u"Test Fundraising Organization")
        organization_obj = self.portal['test_organization']

        organization_obj.invokeFactory('campaign_personal', 'test_campaign_personal', title=u"Test Fundraising Campaign and Personal Fundraiser")
        campaign_personal_obj = organization_obj['test_campaign_personal']

        campaign_personal_obj.invokeFactory('fundraising_page', 'test_page', title=u"Test Fundraising Page")
        page_obj = campaign_personal_obj['test_page']

        organization = IFundraisingOrganization(organization_obj)
        campaign = IFundraisingCampaign(campaign_personal_obj)
        page = IFundraisingPage(page_obj)
        personal = IPersonalFundraiser(campaign_personal_obj)

        self.check_inheritance(organization, campaign, page, personal)
        self.check_local_only(organization, campaign, page, personal)
