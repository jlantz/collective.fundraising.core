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
from collective.fundraising.core.behaviors.utils import get_local_or_default
from collective.fundraising.core import MessageFactory as _
from collective.fundraising.core.behaviors.interfaces import IFundraisingOrganization

class FundraisingOrganization(object):
    """
       Adapter for Fundraising Organization
    """
    implements(IFundraisingOrganization)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    org_name = get_local_or_default('org_name', IFundraisingOrganization)
    org_logo = get_local_or_default('org_logo', IFundraisingOrganization)
    ask_levels = get_local_or_default('ask_levels', IFundraisingOrganization)
    ask_level  = get_local_or_default('ask_level', IFundraisingOrganization)
    ask_level_recurring = get_local_or_default('ask_level_recurring', IFundraisingOrganization)
    ask_quantities = get_local_or_default('ask_quantities', IFundraisingOrganization)
    ask_quantity = get_local_or_default('ask_quantity', IFundraisingOrganization)
    goal = get_local_or_default('goal', IFundraisingOrganization)
    image = get_local_or_default('image', IFundraisingOrganization)
    thank_you = get_local_or_default('thank_you', IFundraisingOrganization)
    receipt_footer = get_local_or_default('receipt_footer', IFundraisingOrganization)
    email_thank_you = get_local_or_default('email_thank_you', IFundraisingOrganization)
    email_dedication = get_local_or_default('email_dedication', IFundraisingOrganization)
    email_pf_created = get_local_or_default('email_pf_created', IFundraisingOrganization)
    email_pf_donation = get_local_or_default('email_pf_donation', IFundraisingOrganization)
    list_fundraiser = get_local_or_default('list_fundraiser', IFundraisingOrganization)
    list_donor = get_local_or_default('list_donor', IFundraisingOrganization)
    allow_pf = get_local_or_default('allow_pf', IFundraisingOrganization)
    goal = get_local_or_default('goal', IFundraisingOrganization)
    pf_goal = get_local_or_default('pf_goal', IFundraisingOrganization)
    pf_appeal = get_local_or_default('pf_appeal', IFundraisingOrganization)
    pf_thank_you = get_local_or_default('pf_thank_you', IFundraisingOrganization)
    completion_threshold = get_local_or_default('completion_threshold', IFundraisingOrganization)
    pf_completion_threshold = get_local_or_default('pf_completion_threshold', IFundraisingOrganization)
