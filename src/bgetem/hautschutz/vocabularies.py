# -*- coding:utf-8 -*-

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

desinf_anwendung = SimpleVocabulary((
    SimpleTerm(value=u'haende', token=u'haende', title=u'Hände'),
    ))

desinf_produktgruppe = SimpleVocabulary((
    SimpleTerm(value=u'haendewaschprodukt', token=u'haendewaschprodukt', title=u"Hygienisches Händewaschprodukt"),
    SimpleTerm(value=u'haendedesinketionsmittel', token=u'haendedesinfektionsmittel', title=u'Händedesinfektionsmittel'),
    ))

