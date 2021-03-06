# -*- coding: utf-8 -*-
from bgetem.hautschutz.content.hautschutzmittel import IHautschutzmittel  # NOQA E501
from bgetem.hautschutz.testing import BGETEM_HAUTSCHUTZ_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class HautschutzmittelIntegrationTest(unittest.TestCase):

    layer = BGETEM_HAUTSCHUTZ_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_hautschutzmittel_schema(self):
        fti = queryUtility(IDexterityFTI, name='Hautschutzmittel')
        schema = fti.lookupSchema()
        self.assertEqual(IHautschutzmittel, schema)

    def test_ct_hautschutzmittel_fti(self):
        fti = queryUtility(IDexterityFTI, name='Hautschutzmittel')
        self.assertTrue(fti)

    def test_ct_hautschutzmittel_factory(self):
        fti = queryUtility(IDexterityFTI, name='Hautschutzmittel')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IHautschutzmittel.providedBy(obj),
            u'IHautschutzmittel not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_hautschutzmittel_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Hautschutzmittel',
            id='hautschutzmittel',
        )

        self.assertTrue(
            IHautschutzmittel.providedBy(obj),
            u'IHautschutzmittel not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('hautschutzmittel', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('hautschutzmittel', parent.objectIds())

    def test_ct_hautschutzmittel_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Hautschutzmittel')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_hautschutzmittel_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Hautschutzmittel')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'hautschutzmittel_id',
            title='Hautschutzmittel container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
