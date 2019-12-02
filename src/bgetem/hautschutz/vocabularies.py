# -*- coding:utf-8 -*-

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from bgetem.hautschutz import _

desinf_anwendung = SimpleVocabulary((
    SimpleTerm(value=u'haende', token=u'haende', title=_(u'Hände')),
    ))

desinf_produktgruppe = SimpleVocabulary((
    SimpleTerm(value=u'haendewaschprodukt', token=u'haendewaschprodukt', title=u"Hygienisches Händewaschprodukt"),
    SimpleTerm(value=u'haendedesinketionsmittel', token=u'haendedesinfektionsmittel', title=u'Händedesinfektionsmittel'),
    ))

desinf_wirksamkeit = SimpleVocabulary((
    SimpleTerm(value=u'bakterizid', token=u'bakterizid', title=_(u'Bakterizid (d.h. wirksam gegen Bakterien, ohne bakterielle Sporen)')),
    SimpleTerm(value=u'begrenzt_viruzid', token=u'begrenzt_viruzid', title=_(u'Begrenzt viruzid PLUS')),
    SimpleTerm(value=u'levurozide', token=u'levurozide', title=_(u'Levurozide (d.h. wirksam gegen Hefen, Sporen)')),
    SimpleTerm(value=u'mykobakterizid', token=u'mykobakterizid', title=_(u'Mykobakterizid')),
    SimpleTerm(value=u'fungizid', token=u'fungizid', title=_(u'Fungizid (d.h. wirksam gegen Schimmelpilze und deren Sporen, z.B.: Aspergillus)')),
    SimpleTerm(value=u'viruzid', token=u'viruzid', title=_(u'Viruswirksamkeit (d.h. begrenzt viruzid oder viruzid gemäß den Anordnungen nach RKI/DVV (2))'))
    ))

desinf_wirksamkeit = SimpleVocabulary((
    SimpleTerm(value=u'bakterizid', token=u'bakterizid', title=_(u'Bakterizid (d.h. wirksam gegen Bakterien, ohne bakterielle Sporen)')),
    SimpleTerm(value=u'begrenzt_viruzid', token=u'begrenzt_viruzid', title=_(u'Begrenzt viruzid PLUS')),
    SimpleTerm(value=u'levurozide', token=u'levurozide', title=_(u'Levurozide (d.h. wirksam gegen Hefen, Sporen)')),
    SimpleTerm(value=u'mykobakterizid', token=u'mykobakterizid', title=_(u'Mykobakterizid')),
    SimpleTerm(value=u'fungizid', token=u'fungizid', title=_(u'Fungizid (d.h. wirksam gegen Schimmelpilze und deren Sporen, z.B.: Aspergillus)')),
    SimpleTerm(value=u'viruzid', token=u'viruzid', title=_(u'Viruswirksamkeit (d.h. begrenzt viruzid oder viruzid gemäß den Anordnungen nach RKI/DVV (2))'))
    ))

einwirkzeit = SimpleVocabulary((
    SimpleTerm(value=u"auswahl", token=u"auswahl", title=_(u"bitte auswählen")),
    SimpleTerm(value=u"30", token=u"30", title=_(u"30")),
    SimpleTerm(value=u"60", token=u"60", title=_(u"60")),
    ))

desinf_pruefung = SimpleVocabulary((
    SimpleTerm(value=u'vah', token=u'vah', title=_(u'VAH (Verband für Angewandte Hygiene e.V.)')),
    SimpleTerm(value=u'rki', token=u'rki', title=_(u'RKI (Robert Koch Institut)')),
    ))

anwendungVocabulary = SimpleVocabulary((
    SimpleTerm(value=u"id_normal", token=u"id_normal", title=_(u"normal belastete Haut")),
    SimpleTerm(value=u"id_stark", token=u"id_stark", title=_(u"stark belastete Haut")),
    ))

schmutzVocabulary = SimpleVocabulary((
    SimpleTerm(value=u"id_leicht", token=u"id_leicht", title=_(u"leichte Verschmutzung")),
    SimpleTerm(value=u"id_normal", token=u"id_normal", title=_(u"normale Verschmutzung")),
    SimpleTerm(value=u"id_grob", token=u"id_grob", title=_(u"grobe Verschmutzung"))
    ))

hautschutzmittelanwendungen = SimpleVocabulary((
    SimpleTerm(value=u"id_chemisch", token=u"id_chemisch", title=_(u"chemisch")),
    SimpleTerm(value=u"id_biologisch", token=u"id_biologisch", title=_(u"biologisch")),
    SimpleTerm(value=u"id_rauche", token=u"id_rauche", title=_(u"Schweissrauche")),
    SimpleTerm(value=u"id_uvstrahlen", token=u"id_uvstrahlen", title=_(u"UV-Strahlen")),
    ))

zusatzVocabulary = SimpleVocabulary.fromItems((
    (u"gegen Hauterweichung", "id_hauterweichung"),
    (u"keine", "keine")
    ))

hskategorieVocabulary = SimpleVocabulary((
    SimpleTerm(value=u"id_wasserloeslich", token=u"wasserloeslich", title=_(u"gegen wasserlösliche Arbeitsstoffe")),
    SimpleTerm(value=u"id_nichtwasserloeslich", token=u"nichtwasserloeslich", title=(u"gegen wasserunlösliche Arbeitsstoffe")),
    SimpleTerm(value=u"id_wechselnd", token=u"wechselnd", title=(u"gegen wechselnde Arbeitsstoffe"))
    ))

material = SimpleVocabulary((
    SimpleTerm(u"baumwolle", u"baumwolle", u"Baumwolle"),
    SimpleTerm(u"bambus-viskose", u"bambus-viskose", u"Bambus-Viskose"),
    SimpleTerm(u"butylkautschuk", u"butylkautschuk", u"Butylkautschuk (Butyl, IR)"),
    SimpleTerm(u"dyneema", u"dyneema", u"Dyneema"),
    SimpleTerm(u"fluorkautschuk", u"fluorkautschuk", u"Fluorkautschuk (Viton, FKM)"),
    SimpleTerm(u"glasfaser", u"glasfaser", u"Glasfaser"),
    SimpleTerm(u"kevlar", u"kevlar", u"Kevlar"),
    SimpleTerm(u"naturkautschuk", u"naturkautschuk", u"Naturkautschuk (Latex, NR)"),
    SimpleTerm(u"nitrilkautschuk", u"nitrilkautschuk", u"Nitrilkautschuk (Nitril, NBR)"),
    SimpleTerm(u"nylon", u"nylon", u"Nylon"),
    SimpleTerm(u"para-aramid", u"para-aramid", u"Para-Aramid"),
    SimpleTerm(u"polyamid", u"polyamid", u"Polyamid"),
    SimpleTerm(u"polychloropren", u"polychloropren", u"Polychloropren (Neopren, CR)"),
    SimpleTerm(u"polyester", u"polyester", u"Polyester"),
    SimpleTerm(u"polyurethan", u"polyurethan", u"Polyurethan (PU)"),
    SimpleTerm(u"polyvinylalkohol", u"polyvinylalkohol", u"Polyvinylalkohol (PVA)"),
    SimpleTerm(u"polyvinylchlorid", u"polyvinylchlorid", u"Polyvinylchlorid (Vinyl, PVC)"),
    SimpleTerm(u"spectra", u"spectra", u"Spectra"),
    SimpleTerm(u"stahl", u"stahl", u"Stahl"),
    SimpleTerm(u"synthetik-leder", u"synthetik-leder", u"Synthetik-Leder")
    ))
