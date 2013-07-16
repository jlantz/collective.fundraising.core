from Acquisition import aq_base
from plone.app.textfield import RichTextValue
from collective.fundraising.core.utils import strip_field_prefix

# Implementations of default value inheritance for some fields
def get_local_or_default(name):

    def getter(self):
        """Get a field's value using inheritance of [page ->] campaign -> settings """

        # Try page
        page = aq_base(self.context.get_fundraising_campaign_page())
        val = getattr(page, '_%s' % name, None)

        test_val = val
        # check if the output of a rich text field is empty
        if isinstance(val, RichTextValue):
            test_val = val.output
        if test_val is not None:
            return val

        # Use default if no local value
        return self.get_default()

    def setter(self, value):
        if value != self.get_default():
            setattr(self, '_%s' % name, value)

    def deleter(self):
        context = aq_base(self.context)
        if hasattr(context, '_%s' % name):
            delattr(context, '_%s')

    def get_default(self):
        base_name = strip_field_prefix(name)

        # Try campaign if different from page (i.e. personal campaign page or campaign variation)
        campaign = aq_base(self.context.get_fundraising_campaign())
        if campaign != self.context.get_fundraising_campaign_page():
            val = getattr(campaign, 'cf_fc_%s' % base_name, None)
            # convert rich text objects, if present:
            if isinstance(val, RichTextValue):
                val = val.output
            if val is not None:
                return val

        # Try settings if nothing found in the campaign
        settings = get_settings()
        val = getattr(settings, 'cf_fs_%s' % base_name, None)

        return val

    return property(getter, setter, deleter)
