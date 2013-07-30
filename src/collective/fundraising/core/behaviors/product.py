from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements
from collective.fundraising.core import MessageFactory as _
from collective.fundraising.core.behaviors.interfaces import IFundraisingProduct

class FundraisingProduct(object):
    """
       Adapter for Fundraising Product
    """
    implements(IFundraisingProduct)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context
