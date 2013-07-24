from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage

from collective.fundraising.core import MessageFactory as _
from collective.fundraising.core.behaviors.interfaces import IDonation
from collective.fundraising.core.behaviors.utils import get_local_or_default


class Donation(object):
    """
       Adapter for Donation
    """
    implements(IDonation)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    amount = get_local_or_default('amount', IDonation)
    is_recurring = get_local_or_default('is_recurring', IDonation)
    recurring_plan = get_local_or_default('recurring_plan', IDonation)
    is_public = get_local_or_default('is_public', IDonation)
    receipt_sent = get_local_or_default('receipt_sent', IDonation)
    notification_sent = get_local_or_default('notification_sent', IDonation)
    added = get_local_or_default('added', IDonation)

    def get_personal_fundraiser(self):
        raise NotImplementedError

    def get_fundraising_page(self):
        raise NotImplementedError

    def get_fundraising_campaign(self):
        raise NotImplementedError

    def get_fundraising_settings(self):
        raise NotImplementedError
