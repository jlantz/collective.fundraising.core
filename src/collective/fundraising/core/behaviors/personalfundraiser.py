from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage

from collective.fundraising.core import MessageFactory as _
from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser
from collective.fundraising.core.behaviors.utils import get_local_or_default


class PersonalFundraiser(object):
    """
       Adapter for Personal Fundraiser
    """
    implements(IPersonalFundraiser)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    image = get_local_or_default('image', IPersonalFundraiser)
    pf_appeal = get_local_or_default('pf_appeal', IPersonalFundraiser)
    pf_thank_you = get_local_or_default('pf_thank_you', IPersonalFundraiser)
    pf_goal = get_local_or_default('pf_goal', IPersonalFundraiser)
    date_start = get_local_or_default('date_start', IPersonalFundraiser)
    date_end = get_local_or_default('date_end', IPersonalFundraiser)
    total = get_local_or_default('total', IPersonalFundraiser)
    count = get_local_or_default('count', IPersonalFundraiser)
    total_pledged = get_local_or_default('total_pledged', IPersonalFundraiser)
    count_pledged = get_local_or_default('count_pledged', IPersonalFundraiser)
