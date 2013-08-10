from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage

from collective.fundraising.core import MessageFactory as _
from collective.fundraising.core.behaviors.interfaces import IFundraisingOrganization
from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser
from collective.fundraising.core.behaviors.interfaces import IDonor
from collective.fundraising.core.behaviors.interfaces import IDonation
from collective.fundraising.core.behaviors.interfaces import IDedication
from collective.fundraising.core.behaviors.utils import get_local_or_default
from collective.fundraising.core.behaviors.utils import get_nearest_behavior

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

    def get_fundraising_organization(self):
        return get_nearest_behavior(self.context, IFundraisingOrganization)

    def get_fundraising_campaign(self):
        return get_nearest_behavior(self.context, IFundraisingCampaign)

    def get_fundraising_page(self):
        return get_nearest_behavior(self.context, IFundraisingPage)

    def get_personal_fundraiser(self):
        return get_nearest_behavior(self.context, IPersonalFundraiser)

    def get_donor(self):
        return get_nearest_behavior(self.context, IDonor)

    def get_dedication(self):
        return get_nearest_behavior(self.context, IDedication)
