import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from collective.fundraising.core.testing import\
    COLLECTIVE_FUNDRAISING_CORE_INTEGRATION


class TestInheritance(unittest.TestCase):

    layer = COLLECTIVE_FUNDRAISING_CORE_INTEGRATION
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        from plone.dexterity.fti import DexterityFTI

        ### Single behavior types

        # Make settings type providing settings behavior
        fti = DexterityFTI('settings')
        self.portal.portal_types._setObject('settings', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingSettings',)

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

        # Make settings_campaign type providing settings and campaign behaviors
        fti = DexterityFTI('settings_campaign')
        self.portal.portal_types._setObject('settings_campaign', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingSettings',
                         'collective.fundraising.core.behaviors.interfaces.IFundraisingCampaign')

        # Make settings_campaign_page type providing settings, campaign, and page behaviors
        fti = DexterityFTI('settings_campaign_page')
        self.portal.portal_types._setObject('settings_campaign_page', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingSettings',
                         'collective.fundraising.core.behaviors.interfaces.IFundraisingCampaign',
                         'collective.fundraising.core.behaviors.interfaces.IFundraisingPage')

        # Make settings_campaign_page type providing settings, campaign, and personal fundraiser behaviors
        fti = DexterityFTI('settings_campaign_personal')
        self.portal.portal_types._setObject('settings_campaign_personal', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingSettings',
                         'collective.fundraising.core.behaviors.interfaces.IFundraisingCampaign',
                         'collective.fundraising.core.behaviors.interfaces.IPersonalFundraiser')

        # Make settings_campaign_page_personal type providing settings, campaign, page, and personal fundraiser behaviors
        fti = DexterityFTI('settings_campaign_page_personal')
        self.portal.portal_types._setObject('settings_campaign_page_personal', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingSettings',
                         'collective.fundraising.core.behaviors.interfaces.IFundraisingCampaign',
                         'collective.fundraising.core.behaviors.interfaces.IFundraisingPage',
                         'collective.fundraising.core.behaviors.interfaces.IPersonalFundraiser')

        # Make settings_campaign_personal_page type providing settings, campaign, personal fundraiser, and page behaviors
        fti = DexterityFTI('settings_campaign_personal_page')
        self.portal.portal_types._setObject('settings_campaign_personal_page', fti)
        fti.klass = 'plone.dexterity.content.Container'
        fti.filter_content_types = False
        fti.behaviors = ('collective.fundraising.core.behaviors.interfaces.IFundraisingSettings',
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

    def check_inheritance(self, settings, campaign, page, personal, page_personal=None, personal_page=None):
        """ Check the inheritance logic against a set of behavior instances """

        # Check that all subobjects inherit from settings
        settings.goal = 1000
        settings.pf_goal = 100
        self.assertEqual(campaign.goal, 1000)
        self.assertEqual(campaign.pf_goal, 100)
        self.assertEqual(page.goal, 1000)
        if page_personal is not None:
            self.assertEqual(page_personal.goal, 1000)
            self.assertEqual(page_personal.pf_goal, 100)
        self.assertEqual(personal.goal, 1000)
        self.assertEqual(personal.pf_goal, 100)
        if personal_page is not None:
            self.assertEqual(personal_page.goal, 1000)

        # Check that page and personal inherit from campaign
        campaign.goal = 2000
        campaign.pf_goal = 200
        self.assertEqual(page.goal, 2000)
        if page_personal is not None:
            self.assertEqual(page_personal.goal, 2000)
            self.assertEqual(page_personal.pf_goal, 200)
        self.assertEqual(personal.goal, 2000)
        self.assertEqual(personal.pf_goal, 200)
        if personal_page is not None:
            self.assertEqual(personal_page.goal, 2000)

        # Check that personal inherits from page if contained in page
        page.pf_goal = 300
        if page_personal is not None:
            self.assertEqual(page_personal.pf_goal, 300)
       
        # Check that page inherits from personal if contained in personal
        personal.pf_goal = 400
        self.assertEqual(personal.pf_goal, 400)
        if personal_page is not None:
            self.assertEqual(personal_page.pf_goal, 400)
            self.assertEqual(personal_page.goal, 2000)

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
        from collective.fundraising.core.behaviors.interfaces import IFundraisingSettings
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

        self.portal.invokeFactory('settings', 'test_settings', title=u"Test Fundraising Settings")
        settings_obj = self.portal['test_settings']

        settings_obj.invokeFactory('campaign', 'test_campaign', title=u"Test Fundraising Campaign")
        campaign_obj = settings_obj['test_campaign']

        campaign_obj.invokeFactory('fundraising_page', 'test_page', title=u"Test Fundraising Page")
        page_obj = campaign_obj['test_page']

        page_obj.invokeFactory('personal', 'test_page_personal', title=u"Test Page Personal Fundraiser")
        page_personal_obj = page_obj['test_page_personal']

        campaign_obj.invokeFactory('personal', 'test_personal', title=u"Test Personal Fundraiser")
        personal_obj = campaign_obj['test_personal']

        personal_obj.invokeFactory('fundraising_page', 'test_personal_page', title=u"Test Personal Fundraiser Page")
        personal_page_obj = personal_obj['test_personal_page']

        settings = IFundraisingSettings(settings_obj)
        campaign = IFundraisingCampaign(campaign_obj)
        page = IFundraisingPage(page_obj)
        page_personal = IPersonalFundraiser(page_personal_obj)
        personal = IPersonalFundraiser(personal_obj)
        personal_page = IFundraisingPage(personal_page_obj)

        self.check_inheritance(settings, campaign, page, personal, page_personal, personal_page)

    def test_combo_settings_campaign(self):
        from collective.fundraising.core.behaviors.interfaces import IFundraisingSettings
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

        self.portal.invokeFactory('settings_campaign', 'test_settings_campaign', title=u"Test Fundraising Settings and Campaign")
        settings_campaign_obj = self.portal['test_settings_campaign']

        settings_campaign_obj.invokeFactory('fundraising_page', 'test_page', title=u"Test Fundraising Page")
        page_obj = settings_campaign_obj['test_page']

        page_obj.invokeFactory('personal', 'test_page_personal', title=u"Test Page Personal Fundraiser")
        page_personal_obj = page_obj['test_page_personal']

        settings_campaign_obj.invokeFactory('personal', 'test_personal', title=u"Test Personal Fundraiser")
        personal_obj = settings_campaign_obj['test_personal']

        personal_obj.invokeFactory('fundraising_page', 'test_personal_page', title=u"Test Personal Fundraiser Page")
        personal_page_obj = personal_obj['test_personal_page']

        settings = IFundraisingSettings(settings_campaign_obj)
        campaign = IFundraisingCampaign(settings_campaign_obj)
        page = IFundraisingPage(page_obj)
        page_personal = IPersonalFundraiser(page_personal_obj)
        personal = IPersonalFundraiser(personal_obj)
        personal_page = IFundraisingPage(personal_page_obj)

        self.check_inheritance(settings, campaign, page, personal, page_personal, personal_page)

    def test_combo_settings_campaign_page(self):
        from collective.fundraising.core.behaviors.interfaces import IFundraisingSettings
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

        self.portal.invokeFactory('settings_campaign_page', 'test_settings_campaign_page', title=u"Test Fundraising Settings, Campaign, and Page")
        settings_campaign_page_obj = self.portal['test_settings_campaign_page']

        settings_campaign_page_obj.invokeFactory('personal', 'test_personal', title=u"Test Personal Fundraiser")
        personal_obj = settings_campaign_page_obj['test_personal']

        personal_obj.invokeFactory('fundraising_page', 'test_personal_page', title=u"Test Personal Fundraiser Page")
        personal_page_obj = personal_obj['test_personal_page']

        settings = IFundraisingSettings(settings_campaign_page_obj)
        campaign = IFundraisingCampaign(settings_campaign_page_obj)
        page = IFundraisingPage(settings_campaign_page_obj)
        personal = IPersonalFundraiser(personal_obj)
        personal_page = IFundraisingPage(personal_page_obj)

        self.check_inheritance(settings, campaign, page, personal, personal_page=personal_page)

    def test_combo_settings_campaign_personal(self):
        from collective.fundraising.core.behaviors.interfaces import IFundraisingSettings
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

        self.portal.invokeFactory('settings_campaign_personal', 'test_settings_campaign_personal', title=u"Test Fundraising Settings, Campaign, and Personal Fundraiser")
        settings_campaign_personal_obj = self.portal['test_settings_campaign_personal']

        settings_campaign_personal_obj.invokeFactory('fundraising_page', 'test_page', title=u"Test Page")
        page_obj = settings_campaign_personal_obj['test_page']

        settings = IFundraisingSettings(settings_campaign_personal_obj)
        campaign = IFundraisingCampaign(settings_campaign_personal_obj)
        page = IFundraisingPage(page_obj)
        personal = IPersonalFundraiser(settings_campaign_personal_obj)

        self.check_inheritance(settings, campaign, page, personal)

    def test_combo_settings_campaign_personal_page(self):
        from collective.fundraising.core.behaviors.interfaces import IFundraisingSettings
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

        self.portal.invokeFactory('settings_campaign_personal_page', 'test_settings_campaign_personal_page', title=u"Test Fundraising Settings, Campaign, Personal Fundraiser, and Page")
        settings_campaign_personal_page_obj = self.portal['test_settings_campaign_personal_page']

        settings_campaign_personal_page_obj.invokeFactory('fundraising_page', 'test_page', title=u"Test Page")
        page_obj = settings_campaign_personal_page_obj['test_page']

        settings = IFundraisingSettings(settings_campaign_personal_page_obj)
        campaign = IFundraisingCampaign(settings_campaign_personal_page_obj)
        page = IFundraisingPage(settings_campaign_personal_page_obj)
        personal = IPersonalFundraiser(settings_campaign_personal_page_obj)

        self.check_inheritance(settings, campaign, page, personal)

    def test_combo_settings_campaign_page_personal(self):
        from collective.fundraising.core.behaviors.interfaces import IFundraisingSettings
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

        self.portal.invokeFactory('settings_campaign_page_personal', 'test_settings_campaign_page_personal', title=u"Test Fundraising Settings, Campaign, Page and Personal Fundraiser")
        settings_campaign_page_personal_obj = self.portal['test_settings_campaign_page_personal']

        settings_campaign_page_personal_obj.invokeFactory('fundraising_page', 'test_page', title=u"Test Page")
        page_obj = settings_campaign_page_personal_obj['test_page']

        settings = IFundraisingSettings(settings_campaign_page_personal_obj)
        campaign = IFundraisingCampaign(settings_campaign_page_personal_obj)
        page = IFundraisingPage(settings_campaign_page_personal_obj)
        personal = IPersonalFundraiser(settings_campaign_page_personal_obj)

        self.check_inheritance(settings, campaign, page, personal)

    def test_combo_campaign_page_personal(self):
        from collective.fundraising.core.behaviors.interfaces import IFundraisingSettings
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

        self.portal.invokeFactory('settings', 'test_settings', title=u"Test Fundraising Settings")
        settings_obj = self.portal['test_settings']

        settings_obj.invokeFactory('campaign_page_personal', 'test_campaign_page_personal', title=u"Test Fundraising Campaign, Page and Personal Fundraiser")
        campaign_page_personal_obj = settings_obj['test_campaign_page_personal']

        settings = IFundraisingSettings(settings_obj)
        campaign = IFundraisingCampaign(campaign_page_personal_obj)
        page = IFundraisingPage(campaign_page_personal_obj)
        personal = IPersonalFundraiser(campaign_page_personal_obj)

        self.check_inheritance(settings, campaign, page, personal)

    def test_combo_campaign_personal_page(self):
        from collective.fundraising.core.behaviors.interfaces import IFundraisingSettings
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

        self.portal.invokeFactory('settings', 'test_settings', title=u"Test Fundraising Settings")
        settings_obj = self.portal['test_settings']

        settings_obj.invokeFactory('campaign_personal_page', 'test_campaign_personal_page', title=u"Test Fundraising Campaign, Personal Fundraiser, and Page")
        campaign_personal_page_obj = settings_obj['test_campaign_personal_page']

        settings = IFundraisingSettings(settings_obj)
        campaign = IFundraisingCampaign(campaign_personal_page_obj)
        page = IFundraisingPage(campaign_personal_page_obj)
        personal = IPersonalFundraiser(campaign_personal_page_obj)

        self.check_inheritance(settings, campaign, page, personal)

    def test_combo_campaign_page(self):
        from collective.fundraising.core.behaviors.interfaces import IFundraisingSettings
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

        self.portal.invokeFactory('settings', 'test_settings', title=u"Test Fundraising Settings")
        settings_obj = self.portal['test_settings']

        settings_obj.invokeFactory('campaign_page', 'test_campaign_page', title=u"Test Fundraising Campaign and Page")
        campaign_page_obj = settings_obj['test_campaign_page']

        campaign_page_obj.invokeFactory('personal', 'test_personal', title=u"Test Personal Fundraiser")
        personal_obj = campaign_page_obj['test_personal']

        personal_obj.invokeFactory('fundraising_page', 'test_personal_page', title=u"Test Personal Fundraiser Page")
        personal_page_obj = personal_obj['test_personal_page']

        settings = IFundraisingSettings(settings_obj)
        campaign = IFundraisingCampaign(campaign_page_obj)
        page = IFundraisingPage(campaign_page_obj)
        personal = IPersonalFundraiser(personal_obj)
        personal_page = IFundraisingPage(personal_page_obj)

        self.check_inheritance(settings, campaign, page, personal, personal_page=personal_page)

    def test_combo_campaign_personal(self):
        from collective.fundraising.core.behaviors.interfaces import IFundraisingSettings
        from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
        from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
        from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

        self.portal.invokeFactory('settings', 'test_settings', title=u"Test Fundraising Settings")
        settings_obj = self.portal['test_settings']

        settings_obj.invokeFactory('campaign_personal', 'test_campaign_personal', title=u"Test Fundraising Campaign and Personal Fundraiser")
        campaign_personal_obj = settings_obj['test_campaign_personal']

        campaign_personal_obj.invokeFactory('fundraising_page', 'test_page', title=u"Test Fundraising Page")
        page_obj = campaign_personal_obj['test_page']

        settings = IFundraisingSettings(settings_obj)
        campaign = IFundraisingCampaign(campaign_personal_obj)
        page = IFundraisingPage(page_obj)
        personal = IPersonalFundraiser(campaign_personal_obj)

        self.check_inheritance(settings, campaign, page, personal)
