from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage

from collective.fundraising.core import MessageFactory as _
from collective.fundraising.core.behaviors.interfaces import IDonor
from collective.fundraising.core.behaviors.utils import get_local_or_default


class Donor(object):
    """
       Adapter for Donor
    """
    implements(IDonor)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    first_name = get_local_or_default('first_name', IDonor)
    last_name = get_local_or_default('last_name', IDonor)
    email = get_local_or_default('email', IDonor)
    email_opt_in = get_local_or_default('email_opt_in', IDonor)
    phone = get_local_or_default('phone', IDonor)
    address_street = get_local_or_default('address_street', IDonor)
    address_city = get_local_or_default('address_city', IDonor)
    address_state = get_local_or_default('address_state', IDonor)
    address_zip = get_local_or_default('address_zip', IDonor)
    address_country = get_local_or_default('address_country', IDonor)
    is_public = get_local_or_default('public', IDonor)

    def get_donations(self):
        raise NotImplementedError
