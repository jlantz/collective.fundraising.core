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
from collective.fundraising.core.behaviors.interfaces import IDonor
from collective.fundraising.core.behaviors.interfaces import IDonation
from collective.fundraising.core.behaviors.interfaces import IDedication
from collective.fundraising.core.behaviors.utils import get_local_or_default
from collective.fundraising.core.behaviors.utils import get_nearest_behavior


class Dedication(object):
    """
       Adapter for Dedications
    """
    implements(IDedication)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    dedication_type = get_local_or_default('dedication_type', IDedication)
    first_name = get_local_or_default('first_name', IDedication)
    last_name = get_local_or_default('last_name', IDedication)
    message = get_local_or_default('message', IDedication)
    notification_type = get_local_or_default('notification_type', IDedication)
    recipient_first_name = get_local_or_default('recipient_first_name', IDedication)
    recipient_last_name = get_local_or_default('recipient_last_name', IDedication)
    recipient_email = get_local_or_default('recipient_email', IDedication)
    recipient_street_address = get_local_or_default('recipient_street_address', IDedication)
    recipient_city = get_local_or_default('recipient_city', IDedication)
    recipient_state = get_local_or_default('recipient_state', IDedication)
    recipient_zip = get_local_or_default('recipient_zip', IDedication)
    recipient_country = get_local_or_default('recipient_country', IDedication)

    def get_fundraising_settings(self):
        return get_nearest_behavior(self.context, IFundraisingSettings)

    def get_fundraising_campaign(self):
        return get_nearest_behavior(self.context, IFundraisingCampaign)

    def get_fundraising_page(self):
        return get_nearest_behavior(self.context, IFundraisingPage)

    def get_personal_fundraiser(self):
        return get_nearest_behavior(self.context, IPersonalFundraiser)

    def get_donor(self):
        return get_nearest_behavior(self.context, IDonor)

    def get_donation(self):
        return get_nearest_behavior(self.context, IDonation)
