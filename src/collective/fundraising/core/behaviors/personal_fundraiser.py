from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage

from collective.fundraising.core import MessageFactory as _
from collective.fundraising.core.behaviors.interfaces import IFundraisingSettings
from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser
from collective.fundraising.core.behaviors.utils import get_local
from collective.fundraising.core.behaviors.utils import get_local_or_default
from collective.fundraising.core.behaviors.utils import get_nearest_behavior


class PersonalFundraiser(object):
    """
       Adapter for Personal Fundraiser
    """
    implements(IPersonalFundraiser)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    image = get_local_or_default('image', IPersonalFundraiser)
    first_name = get_local_or_default('first_name', IPersonalFundraiser)
    last_name = get_local_or_default('last_name', IPersonalFundraiser)
    pf_appeal = get_local_or_default('pf_appeal', IPersonalFundraiser)
    pf_thank_you = get_local_or_default('pf_thank_you', IPersonalFundraiser)
    pf_goal = get_local_or_default('pf_goal', IPersonalFundraiser)
    date_start = get_local_or_default('date_start', IPersonalFundraiser)
    date_end = get_local_or_default('date_end', IPersonalFundraiser)
    total = get_local('total', IPersonalFundraiser)
    count = get_local('count', IPersonalFundraiser)
    total_pledged = get_local('total_pledged', IPersonalFundraiser)
    count_pledged = get_local('count_pledged', IPersonalFundraiser)

    # Inherited only, these field is not defined in the schema
    goal = get_local_or_default('goal', IPersonalFundraiser)
    thank_you = get_local_or_default('thank_you', IPersonalFundraiser)

    def get_fundraising_settings(self):
        return get_nearest_behavior(self.context, IFundraisingSettings)

    def get_fundraising_campaign(self):
        return get_nearest_behavior(self.context, IFundraisingCampaign)

    def get_fundraising_page(self):
        return get_nearest_behavior(self.context, IFundraisingPage)
