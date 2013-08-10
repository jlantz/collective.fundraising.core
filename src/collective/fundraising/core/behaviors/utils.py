from Acquisition import aq_base
from Acquisition import aq_inner
from Acquisition import aq_parent
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from plone.app.textfield import RichTextValue
from z3c.relationfield.relation import RelationValue
from plone.namedfile.file import NamedBlobImage
from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
from collective.fundraising.core.behaviors.interfaces import IFundraisingOrganization
from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

# Map of which behavior each behavior should consider its parent for
# looking up default values
BEHAVIOR_INHERITANCE_MAP = {
    IFundraisingPage: [IPersonalFundraiser, IFundraisingCampaign,],
    IPersonalFundraiser: [IFundraisingPage, IFundraisingCampaign],
    IFundraisingCampaign: [IFundraisingOrganization,],
}

# Implementations of default value inheritance for some fields
def get_local_or_default(name, binterface):

    def getter(self):
        """ Get a field's value either locally or through inheritance """

        adapted = binterface(self.context, None)
        if adapted is not None:
            val = getattr(aq_base(adapted.context), '%s_%s' % (binterface.__name__, name), None)
            test_val = get_test_val(val)
            if test_val is not None:
                return val

        # If no local value, try inheriting a default
        return get_default(self, name, binterface)

    def setter(self, value):
        """ Only store a value if it is different than the inherited default value """
        if value != get_default(self, name, binterface):
            setattr(self.context, '%s_%s' % (binterface.__name__, name), value)

    def deleter(self):
        if hasattr(self.context, '%s_%s' % (binterface.__name__, name)):
            delattr(self.context, '%s_%s' (binterface.__name__, name))

    return property(getter, setter, deleter)

def get_local(name, binterface):
    
    def getter(self):
        adapted = binterface(self.context, None)
        if adapted is not None:
            return getattr(aq_base(adapted.context), '%s_%s' % (binterface.__name__, name), None)
            
    def setter(self, value):
        """ Only store a value if it is different than the inherited default value """
        setattr(self.context, '%s_%s' % (binterface.__name__, name), value)

    def deleter(self):
        if hasattr(self.context, '%s_%s' % (binterface.__name__, name)):
            delattr(self.context, '%s_%s' (binterface.__name__, name))

    return property(getter, setter, deleter)

def get_test_val(val):
    """ Handle special value types where an attribute needs to be 
        checked for a value.
    """
    test_val = val

    # check if the output of a rich text field is empty
    if isinstance(val, RichTextValue):
        test_val = val.output
        if not test_val:
            return None

    # check if the output of a relation choice field is empty
    if isinstance(val, RelationValue):
        test_val = val.to_id
        if not test_val:
            return None

    # check if the output of a relation choice field is empty
    if isinstance(val, NamedBlobImage):
        test_val = val.filename
        if not test_val:
            return None

    return test_val


def get_default(behavior, name, binterface, last_binterface=None):
    """ Get the inherited default value based on the behavior inheritance map """
    parent_binterfaces = BEHAVIOR_INHERITANCE_MAP.get(binterface, None)
    if parent_binterfaces is None:
        return None
    # Try the parent behaviors in order.  Use the first behavior instance found
    adapted = None
    for parent_binterface in parent_binterfaces:
        adapted = get_nearest_behavior(behavior.context, parent_binterface)
        if adapted is None:
            continue

        # Prevent infinite loops caused by parent mapping
        if parent_binterface == last_binterface:
            continue

        context = aq_base(adapted.context)
        attr = '%s_%s' % (parent_binterface.__name__, name)
        if hasattr(context, attr):
            val = getattr(context, '%s_%s' % (parent_binterface.__name__, name), None)
            test_val = get_test_val(val)

            # Handle instances of None being set as the actual field value
            if test_val is not None:
                return val

        return get_default(adapted, name, parent_binterface, binterface)


def get_nearest_behavior(context, binterface):
    """ Accepts a context and a behavior interface.  Crawls from
        context up the content tree until it either finds an object
        which implements the behavior or hits IPloneSiteRoot.

        If found, returns an instance of the behavior.  Otherwise
        returns None
    """

    behavior = binterface(context, None)
    if behavior is not None:
        return behavior

    if not IPloneSiteRoot.providedBy(context):
        return get_nearest_behavior(aq_parent(aq_inner(context)), binterface)
