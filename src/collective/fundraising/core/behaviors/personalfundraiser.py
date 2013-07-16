from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage

from collective.fundraising.core import MessageFactory as _
from collective.fundraising.core.behaviors.utils import get_local_or_default


class IPersonalFundraiser(model.Schema):
    """
       Marker/Form interface for a Personal Fundraiser
    """

    cf_pf_image = NamedBlobImage(
        title=_(u"Image"),
        description=_(u"Upload an image to use in promoting your fundraiser.  This image will be shown on your fundraising page and when your fundraiser is shared on social networks."),
    )
    cf_pf_appeal = RichText(
        title=_(u"Fundraising Appeal"),
        description=_(u"Provide your pitch for why you're fundraising and what it means to you personally."),
    )
    cf_pf_thank_you = RichText(
        title=_(u"Thank You Message"),
        description=_(u"This message will be included on the thank you page and in thank you emails sent to donors to your fundraiser."),
    )
    cf_pf_goal = schema.Int(
        title=_(u"Fundraising Goal"),
        description=_(u"How much money do you aim to raise?"),
    )
    cf_pf_date_start = schema.Date(
        title=_(u"Start Date"),
        description=_(u"Select the start date of your campaign.  Once the start date passes, your page will show the progress along the campaign's timeline."),
    )
    cf_pf_date_end = schema.Date(
        title=_(u"End Date"),
        description=_(u"Select the end date for your campaign.  Your campaign will display a progress timeline towards the end date."),
    )
    cf_pf_total = schema.Float(
        title=_(u"Total Raised"),
        description=_(u"The total amount of money you have raised."),
    )
    cf_pf_count = schema.Int(
        title=_(u"Number of Donations"),
        description=_(u"The number of donations made to your fundraiser."),
    )
    cf_pf_total_pledged = schema.Float(
        title=_(u"Total Pledged"),
        description=_(u"The total amount of money pledged to your fundraiser including any offline donations which have not yet been received."),
    )
    cf_pf_count_pledged = schema.Int(
        title=_(u"Number of Donations"),
        description=_(u"The number of donations pledged to your fundraiser including any offline donations which have not yet been received."),
    )

alsoProvides(IPersonalFundraiser, IFormFieldProvider)

class PersonalFundraiser(object):
    """
       Adapter for Personal Fundraiser
    """
    implements(IPersonalFundraiser)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    cf_pf_image = get_local_or_default('cf_pf_image')
    cf_pf_personal_appeal = get_local_or_default('cf_pf_personal_appeal')
    cf_pf_thank_you = get_local_or_default('cf_pf_thank_you')
    cf_pf_goal = get_local_or_default('cf_pf_goal')
    cf_pf_date_start = get_local_or_default('cf_pf_date_start')
    cf_pf_date_end = get_local_or_default('cf_pf_date_end')
    cf_pf_total = get_local_or_default('cf_pf_total')
    cf_pf_count = get_local_or_default('cf_pf_count')
    cf_pf_total_pledged = get_local_or_default('cf_pf_total_pledged')
    cf_pf_count_pledged = get_local_or_default('cf_pf_count_pledged')
