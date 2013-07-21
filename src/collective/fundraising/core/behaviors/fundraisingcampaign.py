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

    thank_you = get_local_or_default('thank_you', IFundraisingCampaign) 
    receipt_footer = get_local_or_default('receipt_footer', IFundraisingCampaign)
    goal = get_local_or_default('goal', IFundraisingCampaign)
    date_start = get_local_or_default('date_start', IFundraisingCampaign)
    date_end = get_local_or_default('date_end', IFundraisingCampaign)
    total = get_local_or_default('total', IFundraisingCampaign)
    count = get_local_or_default('count', IFundraisingCampaign)
    total_pledged = get_local_or_default('total_pledged', IFundraisingCampaign)
    count_pledged = get_local_or_default('count_pledged', IFundraisingCampaign)
    total_direct = get_local_or_default('total_direct', IFundraisingCampaign)
    count_direct = get_local_or_default('count_direct', IFundraisingCampaign)
    total_pledged_direct = get_local_or_default('total_pledged_direct', IFundraisingCampaign)
    count_pledged_direct = get_local_or_default('count_pledged_direct', IFundraisingCampaign)
    email_thank_you = get_local_or_default('email_thank_you', IFundraisingCampaign)
    email_honorary = get_local_or_default('email_honorary', IFundraisingCampaign)
    email_memorial = get_local_or_default('email_memorial', IFundraisingCampaign)
    email_pf_created = get_local_or_default('email_pf_created', IFundraisingCampaign)
    email_pf_donation = get_local_or_default('email_pf_donation', IFundraisingCampaign)
    list_fundraiser = get_local_or_default('list_fundraiser', IFundraisingCampaign)
    list_donor = get_local_or_default('list_donor', IFundraisingCampaign)
    allow_pf = get_local_or_default('allow_pf', IFundraisingCampaign)
    pf_goal = get_local_or_default('pf_goal', IFundraisingCampaign)
    pf_appeal = get_local_or_default('pf_appeal', IFundraisingCampaign)
    pf_thank_you = get_local_or_default('pf_thank_you', IFundraisingCampaign)

    def refresh_counts_and_totals(self, children=False):
        return

    def get_fundraising_settings(self):
        settings = IFundraisingSettings(self.context, None)
        if settings is not None:
            return settings

        # FIXME: For now, assume we only go 3 layers deep at most (settings -> campaign -> page)
        parent_context = aq_parent(self.context)
        settings = IFundraisingSettings(parent_context, None)
        if settings is not None:
            return settings

        parent_context = aq_parent(parent_context)
        settings = IFundraisingSettings(parent_context, None)
        return settings
        
