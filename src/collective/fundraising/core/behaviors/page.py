from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements
from plone.namedfile.field import NamedBlobImage

from collective.fundraising.core import MessageFactory as _
from collective.fundraising.core.behaviors.interfaces import IFundraisingSettings
from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser
from collective.fundraising.core.behaviors.utils import get_local
from collective.fundraising.core.behaviors.utils import get_local_or_default
from collective.fundraising.core.behaviors.utils import get_nearest_behavior

class FundraisingPage(object):
    """
       Adapter for Fundraising Page
    """
    implements(IFundraisingPage)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    image = get_local_or_default('image', IFundraisingPage)
    goal = get_local_or_default('goal', IFundraisingPage)
    pf_goal = get_local_or_default('pf_goal', IFundraisingPage)
    date_start = get_local_or_default('date_start', IFundraisingPage)
    date_end = get_local_or_default('date_end', IFundraisingPage)
    total = get_local('total', IFundraisingPage)
    count = get_local('count', IFundraisingPage)
    total_pledged = get_local('total_pledged', IFundraisingPage)
    count_pledged = get_local('count_pledged', IFundraisingPage)

    # Inherited only, these field is not defined in the schema
    thank_you = get_local_or_default('thank_you', IPersonalFundraiser)
    pf_thank_you = get_local_or_default('pf_thank_you', IPersonalFundraiser)

    def get_goal_percent(self):
        if self.total is None or self.goal is None:
            return 0
        return int((self.total / self.goal)*100)

    def get_fundraising_settings(self):
        return get_nearest_behavior(self.context, IFundraisingSettings)

    def get_fundraising_campaign(self):
        return get_nearest_behavior(self.context, IFundraisingCampaign)

    def get_personal_fundraiser(self):
        return get_nearest_behavior(self.context, IPersonalFundraiser)
