# -*- coding: utf-8 -*-
from bgetem.hautschutz.content.hautpflegemittel import IHautpflegemittel  # NOQA E501
from bgetem.hautschutz.testing import BGETEM_HAUTSCHUTZ_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class HautpflegemittelIntegrationTest(unittest.TestCase):

    layer = BGETEM_HAUTSCHUTZ_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_hautpflegemittel_schema(self):
        fti = queryUtility(IDexterityFTI, name='Hautpflegemittel')
        schema = fti.lookupSchema()
        self.assertEqual(IHautpflegemittel, schema)

    def test_ct_hautpflegemittel_fti(self):
        fti = queryUtility(IDexterityFTI, name='Hautpflegemittel')
        self.assertTrue(fti)

    def test_ct_hautpflegemittel_factory(self):
        fti = queryUtility(IDexterityFTI, name='Hautpflegemittel')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IHautpflegemittel.providedBy(obj),
            u'IHautpflegemittel not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_hautpflegemittel_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Hautpflegemittel',
            id='hautpflegemittel',
        )

        self.assertTrue(
            IHautpflegemittel.providedBy(obj),
            u'IHautpflegemittel not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('hautpflegemittel', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('hautpflegemittel', parent.objectIds())

    def test_ct_hautpflegemittel_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Hautpflegemittel')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_hautpflegemittel_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Hautpflegemittel')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'hautpflegemittel_id',
            title='Hautpflegemittel container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
