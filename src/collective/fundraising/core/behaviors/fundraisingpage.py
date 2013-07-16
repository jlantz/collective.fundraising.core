from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements
from plone.namedfile.field import NamedBlobImage

from collective.fundraising.core import MessageFactory as _
from collective.fundraising.core.behaviors.utils import get_local_or_default


class IFundraisingPage(model.Schema):
    """
       Marker/Form interface for Fundraising Page
    """

    cf_fp_image = NamedBlobImage(
        title=_(u"Page Image"),
        description=_(u"Upload an image file to represent this page.  This image is used on the page, in listings, and as the image shown when shared on social networks."),
        required=True,
    )
    cf_fp_goal = schema.Int(
        title=_(u"Goal"),
        description=_(u"The page's fundraising goal."),
        required=False,
    )
    cf_fp_date_start = schema.Date(
        title=_(u"Start Date"),
        description=_(u"The page's start date."),
        required=False,
    )
    cf_fp_date_end = schema.Date(
        title=_(u"End Date"),
        description=_(u"The page's end date."),
        required=False,
    )
    cf_fp_donations_total = schema.Float(
        title=_(u"Total Donations"),
        description=_(u"The sum of all posted donations for this campaign and all sub-campaigns."),
        default=0.0,
    )
    cf_fp_donations_count = schema.Int(
        title=_(u"Number of Donations"),
        description=_(u"The count of all posted donations for this campaigns and all sub-campaigns."),
        default=0,
    )
    cf_fp_donations_total_pledged = schema.Float(
        title=_(u"Total Pledged Donations"),
        description=_(u"The sum of all pledged donations for this campaign and all sub-campaigns which have not yet been marked as posted."),
        default=0.0,
    )
    cf_fp_donations_count_pledged = schema.Int(
        title=_(u"Number of Pledged Donations"),
        description=_(u"The count of all pledged donations for this campaign and all sub-campaigns which have not yet been marked as posted."),
        default=0,
    )

    def refresh_counts_and_totals(self, children=False, parent=False):
        """ Refresh the donation total and count fields based on tallying up donation objects.
            If children is True, refreshes any child campaigns.  If parent is True, crawl up 
            to the parent campaign and refresh from there.

            Returns a list of changed fields on the current object. 
        """
        return []

alsoProvides(IFundraisingPage, IFormFieldProvider)


class FundraisingPage(object):
    """
       Adapter for Fundraising Page
    """
    implements(IFundraisingPage)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    cf_fp_image = get_local_or_default('cf_fp_total')
    cf_fp_goal = get_local_or_default('cf_fp_total')
    cf_fp_start_date = get_local_or_default('cf_fp_start_date')
    cf_fp_end_date = get_local_or_default('cf_fp_end_date')
    cf_fp_total = get_local_or_default('cf_fp_total')
    cf_fp_count = get_local_or_default('cf_fp_count')
    cf_fp_total_pledged = get_local_or_default('cf_fp_total_pledged')
    cf_fp_count_pledged = get_local_or_default('cf_fp_count_pledged')
