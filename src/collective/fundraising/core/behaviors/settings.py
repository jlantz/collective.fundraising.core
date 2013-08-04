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
from collective.fundraising.core.behaviors.interfaces import IFundraisingSettings

class FundraisingSettings(object):
    """
       Adapter for Fundraising Settings
    """
    implements(IFundraisingSettings)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    org_name = get_local_or_default('org_name', IFundraisingSettings)
    org_logo = get_local_or_default('org_logo', IFundraisingSettings)
    ask_levels = get_local_or_default('ask_levels', IFundraisingSettings)
    ask_level  = get_local_or_default('ask_level', IFundraisingSettings)
    ask_level_recurring = get_local_or_default('ask_level_recurring', IFundraisingSettings)
    ask_quantities = get_local_or_default('ask_quantities', IFundraisingSettings)
    ask_quantity = get_local_or_default('ask_quantity', IFundraisingSettings)
    goal = get_local_or_default('goal', IFundraisingSettings)
    image = get_local_or_default('image', IFundraisingSettings)
    thank_you = get_local_or_default('thank_you', IFundraisingSettings)
    receipt_footer = get_local_or_default('receipt_footer', IFundraisingSettings)
    email_thank_you = get_local_or_default('email_thank_you', IFundraisingSettings)
    email_dedication = get_local_or_default('email_dedication', IFundraisingSettings)
    email_pf_created = get_local_or_default('email_pf_created', IFundraisingSettings)
    email_pf_donation = get_local_or_default('email_pf_donation', IFundraisingSettings)
    list_fundraiser = get_local_or_default('list_fundraiser', IFundraisingSettings)
    list_donor = get_local_or_default('list_donor', IFundraisingSettings)
    allow_pf = get_local_or_default('allow_pf', IFundraisingSettings)
    goal = get_local_or_default('goal', IFundraisingSettings)
    pf_goal = get_local_or_default('pf_goal', IFundraisingSettings)
    pf_appeal = get_local_or_default('pf_appeal', IFundraisingSettings)
    pf_thank_you = get_local_or_default('pf_thank_you', IFundraisingSettings)
    completion_threshold = get_local_or_default('completion_threshold', IFundraisingSettings)
    pf_completion_threshold = get_local_or_default('pf_completion_threshold', IFundraisingSettings)
