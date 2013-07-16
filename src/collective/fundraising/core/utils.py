
def strip_field_prefix(name):
    """ Strip the *_*_ field prefix used in behaviors for package/behavior abbreviations """
    return '_'.join(name.split('_')[2:])
