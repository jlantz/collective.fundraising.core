from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import collective.fundraising.core


COLLECTIVE_FUNDRAISING_CORE = PloneWithPackageLayer(
    zcml_package=collective.fundraising.core,
    zcml_filename='testing.zcml',
    gs_profile_id='collective.fundraising.core:testing',
    name="COLLECTIVE_FUNDRAISING_CORE")

COLLECTIVE_FUNDRAISING_CORE_INTEGRATION = IntegrationTesting(
    bases=(COLLECTIVE_FUNDRAISING_CORE, ),
    name="COLLECTIVE_FUNDRAISING_CORE_INTEGRATION")

COLLECTIVE_FUNDRAISING_CORE_FUNCTIONAL = FunctionalTesting(
    bases=(COLLECTIVE_FUNDRAISING_CORE, ),
    name="COLLECTIVE_FUNDRAISING_CORE_FUNCTIONAL")
