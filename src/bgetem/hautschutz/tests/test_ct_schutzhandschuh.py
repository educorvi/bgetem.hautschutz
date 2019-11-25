# -*- coding: utf-8 -*-
from bgetem.hautschutz.content.schutzhandschuh import ISchutzhandschuh  # NOQA E501
from bgetem.hautschutz.testing import BGETEM_HAUTSCHUTZ_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class SchutzhandschuhIntegrationTest(unittest.TestCase):

    layer = BGETEM_HAUTSCHUTZ_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_schutzhandschuh_schema(self):
        fti = queryUtility(IDexterityFTI, name='Schutzhandschuh')
        schema = fti.lookupSchema()
        self.assertEqual(ISchutzhandschuh, schema)

    def test_ct_schutzhandschuh_fti(self):
        fti = queryUtility(IDexterityFTI, name='Schutzhandschuh')
        self.assertTrue(fti)

    def test_ct_schutzhandschuh_factory(self):
        fti = queryUtility(IDexterityFTI, name='Schutzhandschuh')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ISchutzhandschuh.providedBy(obj),
            u'ISchutzhandschuh not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_schutzhandschuh_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Schutzhandschuh',
            id='schutzhandschuh',
        )

        self.assertTrue(
            ISchutzhandschuh.providedBy(obj),
            u'ISchutzhandschuh not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('schutzhandschuh', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('schutzhandschuh', parent.objectIds())

    def test_ct_schutzhandschuh_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Schutzhandschuh')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_schutzhandschuh_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Schutzhandschuh')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'schutzhandschuh_id',
            title='Schutzhandschuh container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
