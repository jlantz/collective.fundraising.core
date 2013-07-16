from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements
from plone.app.textfield import RichText
from z3c.relationfield.schema import RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from collective.fundraising.core.behaviors.utils import get_local_or_default
from collective.fundraising.core import MessageFactory as _


class IFundraisingSettings(model.Schema):
    """
       Marker/Form interface for Fundraising Settings
    """

    cf_fs_org_name = schema.TextLine(
        title=_(u"Organization Name"),
        description=_(u"Enter the name of the recipient organization for donations."),
    )
    cf_fs_org_logo = schema.TextLine(
        title=_(u"Organization Logo"),
        description=_(u"Upload a logo image for the organization."),
    )
    cf_fs_ask_levels = schema.Text(
        title=_(u"Donation Ask Levels"),
        description=_(u"Enter ask levels one per line in the format key|level1,level2 for example: 10|10,25,50,100,200,500.  This could be called by adding ?levels=10 to the url"),
        required=False,
    )
    cf_fs_ask_level  = schema.TextLine(
        title=_(u"Default Ask Level"),
        description=_(u"Enter the key of the ask level to use if a level is not provided in the url"),
        required=False,
    )
    cf_fs_ask_level_recurring = schema.TextLine(
        title=_(u"Default Recurring Ask Level"),
        description=_(u""),
        required=False,
    )
    cf_fs_ask_quantities = schema.Text(
        title=_(u"Product Ask Quantities"),
        description=_(u"Enter ask quantities for products one per line in the format key|level1,level2 for example: 1|1,2,3,5,10,20.  This could be called by adding ?levels=1 to the url"),
        required=False,
    )
    cf_fs_ask_quantity = schema.TextLine(
        title=_(u"Default Ask Quantity"),
        description=_(u"Enter the key of the ask quantity to use if no level is provided in the url"),
        required=False,
    )
    cf_fs_thank_you = RichText(
        title=_(u"Thank You Message"),
        description=_(u"Enter the default thank you message to be shown to donors after a donation along with their receipt and post donation actions.  This message is also sent to the email template for the donation thank you email."),
    )
    cf_fs_receipt_footer = RichText(
        title=_(u"Donation Receipt Footer"),
        description=_(u"Enter any text which should appear at the bottom of a donation's receipt.  This is typically used to provide tax exempt status."),
        required=False,
    )
    cf_fs_goal = schema.Int(
        title=_(u"Default Goal"),
        description=_(u"If provided, the goal field is pre-filled with this value on new campaigns"),
        required=False,
    )
    cf_fs_email_thank_you = RelationChoice(
        title=_(u"Email Template - Thank You"),
        description=_(u"Select the default email template for the donation thank you email sent to donors."),
        source=ObjPathSourceBinder(),
    )
    cf_fs_email_honorary = RelationChoice(
        title=_(u"Email Template - Honorary Notification"),
        description=_(u"Select the default email template for notifying the recipient of an honorary donation where email notification was requested."),
        source=ObjPathSourceBinder(),
    )
    cf_fs_email_memorial = RelationChoice(
        title=_(u"Email Template - Memorial Notification"),
        description=_(u"Select the default email template for notifying the recipient of a memorial donation where email notification was requested."),
        source=ObjPathSourceBinder(),
    )
    cf_fs_email_personal_created = RelationChoice(
        title=_(u"Email Template - Personal Fundraiser Created"),
        description=_(u"Select the default email template to send to supporters after they create a personal fundraiser."),
        source=ObjPathSourceBinder(),
    )
    cf_fs_email_personal_donation = RelationChoice(
        title=_(u"Email Template - Personal Fundraiser Donation"),
        description=_(u"Select the default email template to send to a personal fundraiser when a donation is made to their campaign."),
        source=ObjPathSourceBinder(),
    )
    cf_fs_list_fundraiser = RelationChoice(
        title=_(u"Email List - Fundraisers"),
        description=_(u"If selected, users who create personal fundraisers will be added to this email list."),
        source=ObjPathSourceBinder(),
        required=False,
    )
    cf_fs_list_donor = RelationChoice(
        title=_(u"Email List - Donors"),
        description=_(u"If selected, donors will be added to this email list."),
        source=ObjPathSourceBinder(),
        required=False,
    )
    cf_fs_allow_personal = schema.Bool(
        title=_(u"Allow Personal"),
        description=_(u"The default value for the Allow Personal field on newly created campaigns."),
        required=False,
    )
    cf_fs_goal = schema.Int(
        title=_(u"Default Goal"),
        description=_(u"The default value for the Goal field on newly created campaigns."),
        required=False,
    )
    cf_fs_pf_appeal = RichText(
        title=_(u"Default Personal Fundraising Appeal"),
        description=_(u"The default value for the Default Personal Fundraising Appeal on newly created campaigns."),
        required=False,
    )
    cf_fs_pf_thank_you = RichText(
        title=_(u"Default Personal Fundraising Thank You"),
        description=_(u"The default value for the Default Personal Fundraising Thank You field on newly created campaigns"),
        required=False,
    )
    cf_fs_completion_threshold = schema.Int(
        title=_(u"Campaign Progress Display Threshold"),
        description=_(u"The percent at which the goal progress indicator will be shown on fundraising campaigns."),
        default=20,
    )
    cf_fs_pf_completion_threshold = schema.Int(
        title=_(u"Personal Fundraiser Progress Display Threshold"),
        description=_(u"The percent at which the goal progress indicator will be shown on personal fundraisers."),
        default=0,
    )
    
   

alsoProvides(IFundraisingSettings, IFormFieldProvider)


class FundraisingSettings(object):
    """
       Adapter for Fundraising Settings
    """
    implements(IFundraisingSettings)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    cf_fs_org_name = get_local_or_default('cf_fs_org_name')
    cf_fs_org_logo = get_local_or_default('cf_fs_org_logo')
    cf_fs_ask_levels = get_local_or_default('cf_fs_ask_levels')
    cf_fs_ask_level  = get_local_or_default('cf_fs_ask_level')
    cf_fs_ask_level_recurring = get_local_or_default('cf_fs_ask_level_recurring')
    cf_fs_ask_quantities = get_local_or_default('cf_fs_ask_quantities')
    cf_fs_ask_quantity = get_local_or_default('cf_fs_ask_quantity')
    cf_fs_thank_you = get_local_or_default('cf_fs_thank_you')
    cf_fs_receipt_footer = get_local_or_default('cf_fs_receipt_footer')
    cf_fs_goal = get_local_or_default('cf_fs_goal')
    cf_fs_email_thank_you = get_local_or_default('cf_fs_email_thank_you')
    cf_fs_email_honorary = get_local_or_default('cf_fs_email_honorary')
    cf_fs_email_memorial = get_local_or_default('cf_fs_email_memorial')
    cf_fs_email_personal_created = get_local_or_default('cf_fs_email_personal_created')
    cf_fs_email_personal_donation = get_local_or_default('cf_fs_email_personal_donation')
    cf_fs_list_fundraiser = get_local_or_default('cf_fs_list_fundraiser')
    cf_fs_list_donor = get_local_or_default('cf_fs_list_donor')
    cf_fs_allow_personal = get_local_or_default('cf_fs_allow_personal')
    cf_fs_goal = get_local_or_default('cf_fs_goal')
    cf_fs_pf_appeal = get_local_or_default('cf_fs_pf_appeal')
    cf_fs_pf_thank_you = get_local_or_default('cf_fs_pf_thank_you')
    cf_fs_completion_threshold = get_local_or_default('cf_fs_completion_threshold')
    cf_fs_pf_completion_threshold = get_local_or_default('cf_fs_pf_completion_threshold')
