from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage
from z3c.relationfield.schema import RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from collective.fundraising.core import MessageFactory as _
from collective.fundraising.core.behaviors.utils import get_local_or_default


class IFundraisingCampaign(model.Schema):
    """
       Marker/Form interface for Fundraising Campaign
    """

    cf_fc_image = NamedBlobImage(
        title=_(u"Campaign Image"),
        description=_(u"Upload an image file to represent the campaign.  This image is used on the campaign page, in listings, and as the image shown when shared on social networks."),
        required=True,
    )
    cf_fc_thank_you = RichText(
        title=_(u"Thank You Message"),
        description=_(u"The message to be displayed after a donation on the thank you page along with the receipt.  This message is also passed to the thank you email template."),
    )
    cf_fc_receipt_footer = RichText(
        title=_(u"Receipt Footer"),
        description=_(u"The content of the receipt footer typically used to provide information about the organization's 501c3 status and donation tax deductability."),
        required=False,
    )
    cf_fc_goal = schema.Int(
        title=_(u"Goal"),
        description=_(u"The campaign's fundraising goal."),
        required=False,
    )
    cf_fc_date_start = schema.Date(
        title=_(u"Start Date"),
        description=_(u"The campaign's start date."),
        required=False,
    )
    cf_fc_date_end = schema.Date(
        title=_(u"End Date"),
        description=_(u"The campaign's end date."),
        required=False,
    )
    cf_fc_donations_total = schema.Float(
        title=_(u"Total Donations"),
        description=_(u"The sum of all posted donations for this campaign and all sub-campaigns."),
        default=0.0,
    )
    cf_fc_donations_count = schema.Int(
        title=_(u"Number of Donations"),
        description=_(u"The count of all posted donations for this campaigns and all sub-campaigns."),
        default=0,
    )
    cf_fc_donations_total_pledged = schema.Float(
        title=_(u"Total Pledged Donations"),
        description=_(u"The sum of all pledged donations for this campaign and all sub-campaigns which have not yet been marked as posted."),
        default=0.0,
    )
    cf_fc_donations_count_pledged = schema.Int(
        title=_(u"Number of Pledged Donations"),
        description=_(u"The count of all pledged donations for this campaign and all sub-campaigns which have not yet been marked as posted."),
        default=0,
    )
    cf_fc_donations_total_direct = schema.Float(
        title=_(u"Total Direct Donations"),
        description=_(u"The sum of all posted donations made directly to this campaign, excluding donations to any sub-campaigns."),
        default=0.0,
    )
    cf_fc_donations_count_direct = schema.Int(
        title=_(u"Number of Direct Donations"),
        description=_(u"The count of all posted donations made directly to this campaign, excluding donations to any sub-campaigns."),
        default=0,
    )
    cf_fc_donations_total_pledged_direct = schema.Float(
        title=_(u"Total Pledged Direct Donations"),
        description=_(u"The sum of all pledged donations for this campaign directly, excluding donations to any sub-campaigns, which have not yet been marked as posted."),
        default=0.0,
    )
    cf_fc_donations_total_pledged_direct = schema.Int(
        title=_(u"Number of Pledged Direct Donations"),
        description=_(u"The count of all pledged donations for this campaign directly, excluding donations to any sub-campaigns, which have not yet been marked as posted."),
        default=0,
    )
    cf_fc_email_thank_you = RelationChoice(
        title=_(u"Email Template - Donation Thank You"),
        description=_(u"Select the email template for sending the thank you email with receipt to donors after a donation."),
        source=ObjPathSourceBinder(),
    )
    cf_fc_email_honorary = RelationChoice(
        title=_(u"Email Template - Honorary Notification"),
        description=_(u"Select the email template for sending the notification email to the recipient of an honorary donation if the donor selects email notification"),
        source=ObjPathSourceBinder(),
    )
    cf_fc_email_memorial = RelationChoice(
        title=_(u"Email Template - Memorial Donation"),
        description=_(u"Select the email template for sending the notification email to the recipient of a memorial donation if the donor selects email notification"),
        source=ObjPathSourceBinder(),
    )
    cf_fc_email_personal_created = RelationChoice(
        title=_(u"Email Template - Personal Fundraiser Created"),
        description=_(u"Select the email template for sending to a user who creates a personal fundraiser."),
        source=ObjPathSourceBinder(),
    )
    cf_fc_email_personal_donation = RelationChoice(
        title=_(u"Email Template - Personal Fundraiser Donation"),
        description=_(u"Select the email template for sending a notification to a personal fundraiser when someone donates to their campaign."),
        source=ObjPathSourceBinder(),
    )
    cf_fc_list_fundraiser = RelationChoice(
        title=_(u"Email List - Fundraisers"),
        description=_(u"If provided, users who create a personal fundraiser for this campaign will be added to the selected email list."),
        source=ObjPathSourceBinder(),
        required=False,
    )
    cf_fc_list_donor = RelationChoice(
        title=_(u"Email List - Donors"),
        description=_(u"If provided, donors to this campaign will be added to the selected email list."),
        source=ObjPathSourceBinder(),
        required=False,
    )
    cf_fc_allow_personal = schema.Bool(
        title=_(u"Allow Personal Fundraisers?"),
        description=_(u"Should users be able to create a Personal Fundraiser to raise money towards this campaign's goal"),
        required=False,
    )
    cf_fc_default_personal_goal = schema.Int(
        title=_(u"Default Personal Goal"),
        description=_(u"The default value of the Goal field when creating a new Personal Fundraiser in this campaign."),
        required=False,
    )
    cf_fc_default_personal_appeal = RichText(
        title=_(u"Default Personal Appeal"),
        description=_(u"The default value of the Personal Appeal field when creating a new Personal Fundraiser in this campaign."),
        required=False,
    )
    cf_fc_default_personal_thank_you = RichText(
        title=_(u"Default Personal Thank You"),
        description=_(u"The default value of the Thank You Message field when creating a new Personal Fundraiser in this campaign."),
        required=False,
    )

    def refresh_counts_and_totals(self, children=False):
        """ Refresh the donation total and count fields based on tallying up donation objects """
        pass

alsoProvides(IFundraisingCampaign, IFormFieldProvider)


class FundraisingCampaign(object):
    """
       Adapter for Fundraising Campaign behavior
    """
    implements(IFundraisingCampaign)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    cf_fc_thank_you = get_local_or_default('cf_fc_thank_you') 
    cf_fc_receipt_footer = get_local_or_default('cf_fc_receipt_footer')
    cf_fc_goal = get_local_or_default('cf_fc_goal')
    cf_fc_date_start = get_local_or_default('cf_fc_date_start')
    cf_fc_date_end = get_local_or_default('cf_fc_date_end')
    cf_fc_total = get_local_or_default('cf_fc_total')
    cf_fc_count = get_local_or_default('cf_fc_count')
    cf_fc_total_pledged = get_local_or_default('cf_fc_total_pledged')
    cf_fc_count_pledged = get_local_or_default('cf_fc_count_pledged')
    cf_fc_total_direct = get_local_or_default('cf_fc_total_direct')
    cf_fc_count_direct = get_local_or_default('cf_fc_count_direct')
    cf_fc_total_pledged_direct = get_local_or_default('cf_fc_total_pledged_direct')
    cf_fc_count_pledged_direct = get_local_or_default('cf_fc_count_pledged_direct')
    cf_fc_email_thank_you = get_local_or_default('cf_fc_')
    cf_fc_email_honorary = get_local_or_default('cf_fc_')
    cf_fc_email_memorial = get_local_or_default('cf_fc_')
    cf_fc_email_personal_created = get_local_or_default('cf_fc_')
    cf_fc_email_personal_donation = get_local_or_default('cf_fc_')
    cf_fc_list_fundraiser = get_local_or_default('cf_fc_')
    cf_fc_list_donor = get_local_or_default('cf_fc_')
    cf_fc_allow_personal = get_local_or_default('cf_fc_')
    cf_fc_default_personal_goal = get_local_or_default('cf_fc_')
    cf_fc_default_personal_appeal = get_local_or_default('cf_fc_')
    cf_fc_default_personal_thank_you = get_local_or_default('cf_fc_')
