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
from collective.fundraising.core.behaviors.utils import get_local
from collective.fundraising.core.behaviors.utils import get_local_or_default
from collective.fundraising.core.behaviors.utils import get_nearest_behavior
from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
from collective.fundraising.core.behaviors.interfaces import IFundraisingSettings

class FundraisingCampaign(object):
    """
       Adapter for Fundraising Campaign behavior
    """
    implements(IFundraisingCampaign)
    adapts(IDexterityContent)

    def __init__(self, context):
        self.context = context

    image = get_local_or_default('image', IFundraisingCampaign) 
    thank_you = get_local_or_default('thank_you', IFundraisingCampaign) 
    receipt_footer = get_local_or_default('receipt_footer', IFundraisingCampaign)
    goal = get_local_or_default('goal', IFundraisingCampaign)
    date_start = get_local_or_default('date_start', IFundraisingCampaign)
    date_end = get_local_or_default('date_end', IFundraisingCampaign)
    total = get_local('total', IFundraisingCampaign)
    count = get_local('count', IFundraisingCampaign)
    total_pledged = get_local('total_pledged', IFundraisingCampaign)
    count_pledged = get_local('count_pledged', IFundraisingCampaign)
    total_direct = get_local('total_direct', IFundraisingCampaign)
    count_direct = get_local('count_direct', IFundraisingCampaign)
    total_pledged_direct = get_local('total_pledged_direct', IFundraisingCampaign)
    count_pledged_direct = get_local('count_pledged_direct', IFundraisingCampaign)
    email_thank_you = get_local_or_default('email_thank_you', IFundraisingCampaign)
    email_dedication = get_local_or_default('email_dedication', IFundraisingCampaign)
    email_pf_created = get_local_or_default('email_pf_created', IFundraisingCampaign)
    email_pf_donation = get_local_or_default('email_pf_donation', IFundraisingCampaign)
    list_fundraiser = get_local_or_default('list_fundraiser', IFundraisingCampaign)
    list_donor = get_local_or_default('list_donor', IFundraisingCampaign)
    allow_pf = get_local_or_default('allow_pf', IFundraisingCampaign)
    pf_goal = get_local_or_default('pf_goal', IFundraisingCampaign)
    pf_appeal = get_local_or_default('pf_appeal', IFundraisingCampaign)
    pf_thank_you = get_local_or_default('pf_thank_you', IFundraisingCampaign)

    def get_fundraising_settings(self):
        return get_nearest_behavior(self.context, IFundraisingSettings)
       
    def get_goal_percent(self):
        if self.total is None or self.goal is None:
            return 0
        return int((self.total / self.goal)*100) 
