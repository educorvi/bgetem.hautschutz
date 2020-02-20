# -*- coding: utf-8 -*-
from bgetem.hautschutz.content.taetigkeit import ITaetigkeit  # NOQA E501
from bgetem.hautschutz.testing import BGETEM_HAUTSCHUTZ_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class TaetigkeitIntegrationTest(unittest.TestCase):

    layer = BGETEM_HAUTSCHUTZ_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_taetigkeit_schema(self):
        fti = queryUtility(IDexterityFTI, name='Taetigkeit')
        schema = fti.lookupSchema()
        self.assertEqual(ITaetigkeit, schema)

    def test_ct_taetigkeit_fti(self):
        fti = queryUtility(IDexterityFTI, name='Taetigkeit')
        self.assertTrue(fti)

    def test_ct_taetigkeit_factory(self):
        fti = queryUtility(IDexterityFTI, name='Taetigkeit')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ITaetigkeit.providedBy(obj),
            u'ITaetigkeit not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_taetigkeit_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Taetigkeit',
            id='taetigkeit',
        )

        self.assertTrue(
            ITaetigkeit.providedBy(obj),
            u'ITaetigkeit not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('taetigkeit', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('taetigkeit', parent.objectIds())

    def test_ct_taetigkeit_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Taetigkeit')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_taetigkeit_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Taetigkeit')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'taetigkeit_id',
            title='Taetigkeit container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
