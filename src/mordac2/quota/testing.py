# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import mordac2.quota


class Mordac2QuotaLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=mordac2.quota)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'mordac2.quota:default')


MORDAC2_QUOTA_FIXTURE = Mordac2QuotaLayer()


MORDAC2_QUOTA_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MORDAC2_QUOTA_FIXTURE,),
    name='Mordac2QuotaLayer:IntegrationTesting',
)


MORDAC2_QUOTA_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MORDAC2_QUOTA_FIXTURE,),
    name='Mordac2QuotaLayer:FunctionalTesting',
)


MORDAC2_QUOTA_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MORDAC2_QUOTA_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='Mordac2QuotaLayer:AcceptanceTesting',
)
