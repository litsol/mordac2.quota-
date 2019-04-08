# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from mordac2.quota.testing import MORDAC2_QUOTA_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that mordac2.quota is properly installed."""

    layer = MORDAC2_QUOTA_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if mordac2.quota is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'mordac2.quota'))

    def test_browserlayer(self):
        """Test that IMordac2QuotaLayer is registered."""
        from mordac2.quota.interfaces import (
            IMordac2QuotaLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IMordac2QuotaLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MORDAC2_QUOTA_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['mordac2.quota'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if mordac2.quota is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'mordac2.quota'))

    def test_browserlayer_removed(self):
        """Test that IMordac2QuotaLayer is removed."""
        from mordac2.quota.interfaces import \
            IMordac2QuotaLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IMordac2QuotaLayer,
            utils.registered_layers())
