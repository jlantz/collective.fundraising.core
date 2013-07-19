from collective.fundraising.core.testing import COLLECTIVE_FUNDRAISING_CORE_FUNCTIONAL
from plone.testing import layered
import robotsuite
import unittest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite("test_behaviors.robot"),
                layer=COLLECTIVE_FUNDRAISING_CORE_FUNCTIONAL)
    ])
    return suite
