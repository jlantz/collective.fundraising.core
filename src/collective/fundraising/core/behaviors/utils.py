from Acquisition import aq_base
from plone.app.textfield import RichTextValue
from collective.fundraising.core.behaviors.interfaces import IFundraisingCampaign
from collective.fundraising.core.behaviors.interfaces import IFundraisingPage
from collective.fundraising.core.behaviors.interfaces import IFundraisingSettings
from collective.fundraising.core.behaviors.interfaces import IPersonalFundraiser

# Map of which behavior each behavior should consider its parent for
# looking up default values
BEHAVIOR_INHERITANCE_MAP = {
    IFundraisingPage: IFundraisingCampaign,
    IPersonalFundraiser: IPersonalFundraiser,
    IFundraisingCampaign: IFundraisingSettings,
    IFundraisingSettings: None,
}

# Implementations of default value inheritance for some fields
def get_local_or_default(name, binterface):

    def getter(self):
        """ Get a field's value either locally or through inheritance """

        adapted = binterface(self.context, None)
        if adapted is not None:
            val = getattr(adapted.context, '%s_%s' % (binterface.__name__, name), None)
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
    return test_val


def get_default(behavior, name, binterface):
    """ Get the inherited default value based on the behavior inheritance map """
    parent_binterface = BEHAVIOR_INHERITANCE_MAP.get(binterface, None)
    if parent_binterface is None:
        return None

    adapted = parent_binterface(behavior.context, None)
    if adapted is None:
        return None

    val = getattr(adapted.context, '%s_%s' % (binterface.__name__, name), None)
    if val is None:
        return None

    test_val = get_test_val(val)
    if test_val is None:
        return None

    return val
