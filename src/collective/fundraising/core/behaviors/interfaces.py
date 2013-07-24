from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements
from plone.supermodel import model
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage
from z3c.relationfield.schema import RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from collective.fundraising.core import MessageFactory as _


class IFundraisingCampaign(model.Schema):
    """
       Marker/Form interface for Fundraising Campaign
    """

    image = NamedBlobImage(
        title=_(u"Campaign Image"),
        description=_(u"Upload an image file to represent the campaign.  This image is used on the campaign page, in listings, and as the image shown when shared on social networks."),
        required=False,
    )
    thank_you = RichText(
        title=_(u"Thank You Message"),
        description=_(u"The message to be displayed after a donation on the thank you page along with the receipt.  This message is also passed to the thank you email template."),
        required=False,
    )
    receipt_footer = RichText(
        title=_(u"Receipt Footer"),
        description=_(u"The content of the receipt footer typically used to provide information about the organization's 501c3 status and donation tax deductability."),
        required=False,
    )
    goal = schema.Int(
        title=_(u"Goal"),
        description=_(u"The campaign's fundraising goal."),
        required=False,
    )
    date_start = schema.Date(
        title=_(u"Start Date"),
        description=_(u"The campaign's start date."),
        required=False,
    )
    date_end = schema.Date(
        title=_(u"End Date"),
        description=_(u"The campaign's end date."),
        required=False,
    )
    total = schema.Float(
        title=_(u"Total Donations"),
        description=_(u"The sum of all posted donations for this campaign and all sub-campaigns."),
        default=0.0,
    )
    count = schema.Int(
        title=_(u"Number of Donations"),
        description=_(u"The count of all posted donations for this campaigns and all sub-campaigns."),
        default=0,
    )
    total_pledged = schema.Float(
        title=_(u"Total Pledged Donations"),
        description=_(u"The sum of all pledged donations for this campaign and all sub-campaigns which have not yet been marked as posted."),
        default=0.0,
    )
    count_pledged = schema.Int(
        title=_(u"Number of Pledged Donations"),
        description=_(u"The count of all pledged donations for this campaign and all sub-campaigns which have not yet been marked as posted."),
        default=0,
    )
    total_direct = schema.Float(
        title=_(u"Total Direct Donations"),
        description=_(u"The sum of all posted donations made directly to this campaign, excluding donations to any sub-campaigns."),
        default=0.0,
    )
    count_direct = schema.Int(
        title=_(u"Number of Direct Donations"),
        description=_(u"The count of all posted donations made directly to this campaign, excluding donations to any sub-campaigns."),
        default=0,
    )
    total_pledged_direct = schema.Float(
        title=_(u"Total Pledged Direct Donations"),
        description=_(u"The sum of all pledged donations for this campaign directly, excluding donations to any sub-campaigns, which have not yet been marked as posted."),
        default=0.0,
    )
    total_pledged_direct = schema.Int(
        title=_(u"Number of Pledged Direct Donations"),
        description=_(u"The count of all pledged donations for this campaign directly, excluding donations to any sub-campaigns, which have not yet been marked as posted."),
        default=0,
    )
    email_thank_you = RelationChoice(
        title=_(u"Email Template - Donation Thank You"),
        description=_(u"Select the email template for sending the thank you email with receipt to donors after a donation."),
        source=ObjPathSourceBinder(),
        required=False,
    )
    email_honorary = RelationChoice(
        title=_(u"Email Template - Honorary Notification"),
        description=_(u"Select the email template for sending the notification email to the recipient of an honorary donation if the donor selects email notification"),
        source=ObjPathSourceBinder(),
        required=False,
    )
    email_memorial = RelationChoice(
        title=_(u"Email Template - Memorial Donation"),
        description=_(u"Select the email template for sending the notification email to the recipient of a memorial donation if the donor selects email notification"),
        source=ObjPathSourceBinder(),
        required=False,
    )
    email_pf_created = RelationChoice(
        title=_(u"Email Template - Personal Fundraiser Created"),
        description=_(u"Select the email template for sending to a user who creates a personal fundraiser."),
        source=ObjPathSourceBinder(),
        required=False,
    )
    email_pf_donation = RelationChoice(
        title=_(u"Email Template - Personal Fundraiser Donation"),
        description=_(u"Select the email template for sending a notification to a personal fundraiser when someone donates to their campaign."),
        source=ObjPathSourceBinder(),
        required=False,
    )
    list_fundraiser = RelationChoice(
        title=_(u"Email List - Fundraisers"),
        description=_(u"If provided, users who create a personal fundraiser for this campaign will be added to the selected email list."),
        source=ObjPathSourceBinder(),
        required=False,
    )
    list_donor = RelationChoice(
        title=_(u"Email List - Donors"),
        description=_(u"If provided, donors to this campaign will be added to the selected email list."),
        source=ObjPathSourceBinder(),
        required=False,
    )
    allow_pf = schema.Bool(
        title=_(u"Allow Personal Fundraisers?"),
        description=_(u"Should users be able to create a Personal Fundraiser to raise money towards this campaign's goal"),
        required=False,
    )
    pf_goal = schema.Int(
        title=_(u"Default Personal Goal"),
        description=_(u"The default value of the Goal field when creating a new Personal Fundraiser in this campaign."),
        required=False,
    )
    pf_appeal = RichText(
        title=_(u"Default Personal Appeal"),
        description=_(u"The default value of the Personal Appeal field when creating a new Personal Fundraiser in this campaign."),
        required=False,
    )
    pf_thank_you = RichText(
        title=_(u"Default Personal Thank You"),
        description=_(u"The default value of the Thank You Message field when creating a new Personal Fundraiser in this campaign."),
        required=False,
    )

    def refresh_counts_and_totals(self, children=False):
        """ Refresh the donation total and count fields based on tallying up donation objects """

    def get_fundraising_pages(self):
        """ Returns a catalog result set of all fundraising pages """

    def get_fundraising_settings(self):
        """ Returns the related IFundraisingSettings behavior instance if it can be found or None """


alsoProvides(IFundraisingCampaign, IFormFieldProvider)


class IFundraisingPage(model.Schema):
    """
       Marker/Form interface for Fundraising Page
    """

    image = NamedBlobImage(
        title=_(u"Page Image"),
        description=_(u"Upload an image file to represent this page.  This image is used on the page, in listings, and as the image shown when shared on social networks."),
        required=False,
    )
    goal = schema.Int(
        title=_(u"Goal"),
        description=_(u"The page's fundraising goal."),
        required=False,
    )
    date_start = schema.Date(
        title=_(u"Start Date"),
        description=_(u"The page's start date."),
        required=False,
    )
    date_end = schema.Date(
        title=_(u"End Date"),
        description=_(u"The page's end date."),
        required=False,
    )
    total = schema.Float(
        title=_(u"Total Donations"),
        description=_(u"The sum of all posted donations for this campaign and all sub-campaigns."),
        default=0.0,
    )
    count = schema.Int(
        title=_(u"Number of Donations"),
        description=_(u"The count of all posted donations for this campaigns and all sub-campaigns."),
        default=0,
    )
    total_pledged = schema.Float(
        title=_(u"Total Pledged Donations"),
        description=_(u"The sum of all pledged donations for this campaign and all sub-campaigns which have not yet been marked as posted."),
        default=0.0,
    )
    count_pledged = schema.Int(
        title=_(u"Number of Pledged Donations"),
        description=_(u"The count of all pledged donations for this campaign and all sub-campaigns which have not yet been marked as posted."),
        default=0,
    )

    def refresh_counts_and_totals(self, children=False, parent=False):
        """ Refresh the donation total and count fields based on tallying up donation objects.
            If children is True, refreshes any child campaigns.  If parent is True, crawl up 
            to the parent campaign and refresh from there.

            Returns a list of changed fields on the current object. 
        """
        return []

    def get_fundraising_campaign(self):
        """ Returns the related IFundraisingCampaign behavior instance if it can be found or None """

    def get_fundraising_settings(self):
        """ Returns the related IFundraisingSettings behavior instance if it can be found or None """


alsoProvides(IFundraisingPage, IFormFieldProvider)


class IFundraisingProduct(model.Schema):
    """
       Marker/Form interface for Fundraising Product
    """

alsoProvides(IFundraisingProduct, IFormFieldProvider)


class IFundraisingSettings(model.Schema):
    """
       Marker/Form interface for Fundraising Settings
    """

    org_name = schema.TextLine(
        title=_(u"Organization Name"),
        description=_(u"Enter the name of the recipient organization for donations."),
    )
    org_logo = NamedBlobImage(
        title=_(u"Organization Logo"),
        description=_(u"Upload a logo image for the organization."),
        required=False,
    )
    ask_levels = schema.Text(
        title=_(u"Donation Ask Levels"),
        description=_(u"Enter ask levels one per line in the format key|level1,level2 for example: 10|10,25,50,100,200,500.  This could be called by adding ?levels=10 to the url"),
        required=False,
    )
    ask_level  = schema.TextLine(
        title=_(u"Default Ask Level"),
        description=_(u"Enter the key of the ask level to use if a level is not provided in the url"),
        required=False,
    )
    ask_level_recurring = schema.TextLine(
        title=_(u"Default Recurring Ask Level"),
        description=_(u""),
        required=False,
    )
    ask_quantities = schema.Text(
        title=_(u"Product Ask Quantities"),
        description=_(u"Enter ask quantities for products one per line in the format key|level1,level2 for example: 1|1,2,3,5,10,20.  This could be called by adding ?levels=1 to the url"),
        required=False,
    )
    ask_quantity = schema.TextLine(
        title=_(u"Default Ask Quantity"),
        description=_(u"Enter the key of the ask quantity to use if no level is provided in the url"),
        required=False,
    )
    thank_you = RichText(
        title=_(u"Thank You Message"),
        description=_(u"Enter the default thank you message to be shown to donors after a donation along with their receipt and post donation actions.  This message is also sent to the email template for the donation thank you email."),
        required=False,
    )
    receipt_footer = RichText(
        title=_(u"Donation Receipt Footer"),
        description=_(u"Enter any text which should appear at the bottom of a donation's receipt.  This is typically used to provide tax exempt status."),
        required=False,
    )
    goal = schema.Int(
        title=_(u"Default Goal"),
        description=_(u"If provided, the goal field is pre-filled with this value on new campaigns"),
        required=False,
    )
    pf_goal = schema.Int(
        title=_(u"Default Personal Goal"),
        description=_(u"The default value of the Goal field when creating a new Personal Fundraiser."),
        required=False,
    )
    email_thank_you = RelationChoice(
        title=_(u"Email Template - Thank You"),
        description=_(u"Select the default email template for the donation thank you email sent to donors."),
        source=ObjPathSourceBinder(),
        required=False,
    )
    email_honorary = RelationChoice(
        title=_(u"Email Template - Honorary Notification"),
        description=_(u"Select the default email template for notifying the recipient of an honorary donation where email notification was requested."),
        source=ObjPathSourceBinder(),
        required=False,
    )
    email_memorial = RelationChoice(
        title=_(u"Email Template - Memorial Notification"),
        description=_(u"Select the default email template for notifying the recipient of a memorial donation where email notification was requested."),
        source=ObjPathSourceBinder(),
        required=False,
    )
    email_pf_created = RelationChoice(
        title=_(u"Email Template - Personal Fundraiser Created"),
        description=_(u"Select the default email template to send to supporters after they create a personal fundraiser."),
        source=ObjPathSourceBinder(),
        required=False,
    )
    email_pf_donation = RelationChoice(
        title=_(u"Email Template - Personal Fundraiser Donation"),
        description=_(u"Select the default email template to send to a personal fundraiser when a donation is made to their campaign."),
        source=ObjPathSourceBinder(),
        required=False,
    )
    list_fundraiser = RelationChoice(
        title=_(u"Email List - Fundraisers"),
        description=_(u"If selected, users who create personal fundraisers will be added to this email list."),
        source=ObjPathSourceBinder(),
        required=False,
    )
    list_donor = RelationChoice(
        title=_(u"Email List - Donors"),
        description=_(u"If selected, donors will be added to this email list."),
        source=ObjPathSourceBinder(),
        required=False,
    )
    allow_pf = schema.Bool(
        title=_(u"Allow Personal"),
        description=_(u"The default value for the Allow Personal field on newly created campaigns."),
        required=False,
    )
    goal = schema.Int(
        title=_(u"Default Goal"),
        description=_(u"The default value for the Goal field on newly created campaigns."),
        required=False,
    )
    pf_appeal = RichText(
        title=_(u"Default Personal Fundraising Appeal"),
        description=_(u"The default value for the Default Personal Fundraising Appeal on newly created campaigns."),
        required=False,
    )
    pf_thank_you = RichText(
        title=_(u"Default Personal Fundraising Thank You"),
        description=_(u"The default value for the Default Personal Fundraising Thank You field on newly created campaigns"),
        required=False,
    )
    completion_threshold = schema.Int(
        title=_(u"Campaign Progress Display Threshold"),
        description=_(u"The percent at which the goal progress indicator will be shown on fundraising campaigns."),
        default=20,
    )
    pf_completion_threshold = schema.Int(
        title=_(u"Personal Fundraiser Progress Display Threshold"),
        description=_(u"The percent at which the goal progress indicator will be shown on personal fundraisers."),
        default=0,
    )
    
alsoProvides(IFundraisingSettings, IFormFieldProvider)


class IPersonalFundraiser(model.Schema):
    """
       Marker/Form interface for a Personal Fundraiser
    """

    image = NamedBlobImage(
        title=_(u"Image"),
        description=_(u"Upload an image to use in promoting your fundraiser.  This image will be shown on your fundraising page and when your fundraiser is shared on social networks."),
        required=False,
    )
    appeal = RichText(
        title=_(u"Fundraising Appeal"),
        description=_(u"Provide your pitch for why you're fundraising and what it means to you personally."),
        required=False,
    )
    thank_you = RichText(
        title=_(u"Thank You Message"),
        description=_(u"This message will be included on the thank you page and in thank you emails sent to donors to your fundraiser."),
        required=False,
    )
    pf_goal = schema.Int(
        title=_(u"Fundraising Goal"),
        description=_(u"How much money do you aim to raise?"),
        required=False,
    )
    date_start = schema.Date(
        title=_(u"Start Date"),
        description=_(u"Select the start date of your campaign.  Once the start date passes, your page will show the progress along the campaign's timeline."),
        required=False,
    )
    date_end = schema.Date(
        title=_(u"End Date"),
        description=_(u"Select the end date for your campaign.  Your campaign will display a progress timeline towards the end date."),
        required=False,
    )
    total = schema.Float(
        title=_(u"Total Raised"),
        description=_(u"The total amount of money you have raised."),
        default=0.0,
    )
    count = schema.Int(
        title=_(u"Number of Donations"),
        description=_(u"The number of donations made to your fundraiser."),
        default=0,
    )
    total_pledged = schema.Float(
        title=_(u"Total Pledged"),
        description=_(u"The total amount of money pledged to your fundraiser including any offline donations which have not yet been received."),
        default=0.0,
    )
    count_pledged = schema.Int(
        title=_(u"Number of Donations"),
        description=_(u"The number of donations pledged to your fundraiser including any offline donations which have not yet been received."),
        default=0,
    )

    def get_fundraising_page(self):
        """ Returns the related IFundraisingPage behavior instance if it can be found or None """

    def get_fundraising_campaign(self):
        """ Returns the related IFundraisingCampaign behavior instance if it can be found or None """

    def get_fundraising_settings(self):
        """ Returns the related IFundraisingSettings behavior instance if it can be found or None """

alsoProvides(IPersonalFundraiser, IFormFieldProvider)

class IDonor(model.Schema):
    first_name = schema.TextLine(
        title=_(u'First Name'),
        required = False,
    )
    last_name = schema.TextLine(
        title=_(u'Last Name'),
        required = False,
    )
    email = schema.TextLine(
        title=_(u'Email'),
        required = False,
    )
    email_opt_in = schema.Bool(
        title=_(u'Email Opt In'),
        required=False,
    )
    phone = schema.TextLine(
        title=_(u'Phone'),
        required = False,
    )
    address_street = schema.TextLine(
        title=_(u'Street Address'),
        required = False,
    )
    address_city = schema.TextLine(
        title=_(u'City'),
        required = False,
    )
    address_state = schema.TextLine(
        title=_(u'State'),
        required = False,
    )
    address_zip = schema.TextLine(
        title=_(u'Zip Code'),
        required = False,
    )
    address_country = schema.TextLine(
        title=_(u'Country'),
        required = False,
    )
    is_public = schema.Bool(
        title=_(u'Is Public?'),
        description=_(u"Should name and location be visible to the public in listings?"),
        default=True,
        required = False,
    )

    def get_donations(self):
        """ Return the catalog results of all donations by this donor """

alsoProvides(IDonor, IFormFieldProvider)


class IDonation(model.Schema):
    amount = schema.Float(
        title=_(u'Amount'),
    )
    is_recurring = schema.Bool(
        title=u"Is Recurring?",
        description=u"Is this a recurring donation?",
        required=False,
        default=False,
    )
    recurring_plan = schema.TextLine(
        title=u"Recurring Plan",
        description=u"If this is a recurring donation, this is set to the ID of the plan",
        required=False,
    )
    is_public = schema.Bool(
        title=_(u'Is Public?'),
        description=_(u"Should this donation show up in listings such as recent donations?"),
        default=True,
    )
    receipt_sent = schema.Bool(
        title=u"Receipt Sent?",
        description=u"Was an email receipt sent for this donation?  NOTE: This is checked automatically by the system",
        required=False,
        default=False,
    )
    notification_sent = schema.Bool(
        title=u"Notification Sent to Fundraiser?",
        description=u"Was an email notification sent for this donation?  NOTE: This is checked automatically by the system",
        required=False,
        default=False,
    )
    added = schema.Bool(
        title=u"Added to Campaign?",
        description=u"Was this donation added to the totals for the campaign?  NOTE: This is checked automatically by the system",
        required=False,
        default=False,
    )

    def get_fundraising_settings(self):
        """ Returns the related IFundraisingSettings behavior instance if it can be found or None """

    def get_fundraising_campaign(self):
        """ Returns the related IFundraisingCampaign behavior instance if it can be found or None """

    def get_fundraising_page(self):
        """ Returns the related IFundraisingPage behavior instance if it can be found or None """

    def get_personal_fundraiser(self):
        """ Returns the related IPersonalFundraiser behavior instance if it can be found or None """

    def get_donor(self):
        """ Returns the related IDonor behavior instance if it can be found or None """

alsoProvides(IDonation, IFormFieldProvider)
