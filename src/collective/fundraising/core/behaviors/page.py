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
    start_date = get_local_or_default('start_date', IFundraisingPage)
    end_date = get_local_or_default('end_date', IFundraisingPage)
    total = get_local_or_default('total', IFundraisingPage)
    count = get_local_or_default('count', IFundraisingPage)
    total_pledged = get_local_or_default('total_pledged', IFundraisingPage)
    count_pledged = get_local_or_default('count_pledged', IFundraisingPage)

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
