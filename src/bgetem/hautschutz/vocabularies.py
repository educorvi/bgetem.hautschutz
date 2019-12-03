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

symbole_374_alt = [
    SimpleTerm(u'chemikalien_einfach', u'chemikalien_einfach', u'Eingeschränkter Schutz gegen Chemikalien'),
    SimpleTerm(u'chemikalien_spez', u'chemikalien_spez', u'Spezifischer Schutz gegen Chemikalien'),
    SimpleTerm(u'bakt_pilze', u'bakt_pilze', u'Schutz gegen Mikroorganismen (Bakterien und Pilze)'),
]
pruefung374alt = SimpleVocabulary(symbole_374_alt)

profilierung = SimpleVocabulary ((
    SimpleTerm(u"Fingerspitzen Diamantprofil", u"Fingerspitzen Diamantprofil", u"Fingerspitzen Diamantprofil"),
    SimpleTerm(u"Fingerspitzen genoppt", u"Fingerspitzen genoppt", u"Fingerspitzen genoppt"),
    SimpleTerm(u"Fingerspitzen geraut", u"Fingerspitzen geraut", u"Fingerspitzen geraut"),
    SimpleTerm(u"Fingerspitzen glatt", u"Fingerspitzen glatt", u"Fingerspitzen glatt"),
    SimpleTerm(u"Fingerspitzen mit Profil", u"Fingerspitzen mit Profil", u"Fingerspitzen mit Profil"),
    SimpleTerm(u"Fingerspitzen Rautenprofil", u"Fingerspitzen Rautenprofil", u"Fingerspitzen Rautenprofil"),
    SimpleTerm(u"Handfleache Diamantprofil", u"Handfleache Diamantprofil", u"Handfläche Diamantprofil"),
    SimpleTerm(u"Handflaeche genoppt", u"Handflaeche genoppt", u"Handfläche genoppt"),
    SimpleTerm(u"Handflaeche geraut", u"Handflaeche geraut", u"Handfläche geraut"),
    SimpleTerm(u"Handflaeche glatt", u"Handflaeche glatt", u"Handfläche glatt"),
    SimpleTerm(u"Handflaeche mit Profil", u"Handflaeche mit Profil", u"Handfläche mit Profil"),
    SimpleTerm(u"Handflaeche Rautenprofil", u"Handflaeche Rautenprofil", u"Handfläche Rautenprofil")
    ))

cecatvalues = SimpleVocabulary((
    SimpleTerm(u"auswahl", u"auswahl", u"bitte auswählen"),
    SimpleTerm(1, 1, u'I'),
    SimpleTerm(2, 2, u'II'),
    SimpleTerm(3, 3, u'III'),
    ))

allergene_vocab = SimpleVocabulary((
    SimpleTerm(u'Thiurame', u'Thiurame', u'Thiurame'),
    SimpleTerm(u'TMTM', u'TMTM', u'Tetramethylthiurammonosulfid (TMTM)'),
    SimpleTerm(u'TMTD', u'TMTD', u'Tetramethylthiuramdisulfid (TMTD)'),
    SimpleTerm(u'TETD', u'TETD', u'Tetraethylthiuramdisulfid (TETD)'),
    SimpleTerm(u'DPTD', u'DPTD', u'Dipentamethylthiuramdisulfid (DPTD)'),
    SimpleTerm(u'Dithiocarbamate', u'Dithiocarbamate', u'Dithiocarbamate'),
    SimpleTerm(u'ZDMC', u'ZDMC', u'Zinkdimethyldithiocarbamat (Ziram, ZDMC)'),
    SimpleTerm(u'ZDEC', u'ZDEC', u'Zinkdiethyldithiocarbamat (ZDC, ZDEC)'),
    SimpleTerm(u'ZDBC', u'ZDBC', u'Zinkdibutyldithiocarbamat (ZBC, ZDBC)'),
    SimpleTerm(u'ZEPC', u'ZEPC', u'Zinkethylphenyldithiocarbamat (ZEPC)'),
    SimpleTerm(u'ZPD', u'ZPD', u'Zinkpentamethylendithiocarbamat (ZPD)'),
    SimpleTerm(u'NBC', u'NBC', u'Natriumdibutyldithiocarbamat (NBC)'),
    SimpleTerm(u'NHEC', u'NHEC', u'Natriumcyclohexylethyldithiocarbamat (NHEC)'),
    SimpleTerm(u'Zinkdibenzyldithiocarbama', u'Zinkdibenzyldithiocarbama', u'Zinkdibenzyldithiocarbama'),
    SimpleTerm(u'Thioharnstoffe', u'Thioharnstoffe', u'Thioharnstoffe'),
    SimpleTerm(u'DBTU', u'DBTU', u'Dibutylthioharnstoff (DBTU)'),
    SimpleTerm(u'DETU', u'DETU', u'Diethylthioharnstoff (DETU)'),
    SimpleTerm(u'DPTU', u'DPTU', u'Diphenylthioharnstoff (DPTU)'),
    SimpleTerm(u'ETU', u'ETU', u"N,N'-Ethylenthioharnstoff (ETU)"),
    SimpleTerm(u'Mercaptobenzothiazol', u'Mercaptobenzothiazol', u'Mercaptobenzothiazol'),
    SimpleTerm(u'MBT', u'MBT', u'Mercaptobenzothiazol (MBT)'),
    SimpleTerm(u'ZMBT', u'ZMBT', u'Zinkmercaptobenzothiazol (ZMBT)'),
    SimpleTerm(u'MBS', u'MBS', u'Morpholinylmercaptobenzothiazol (MOR, MBS)'),
    SimpleTerm(u'MBTS', u'MBTS', u'Dibenzothiazyldisulfid (MBTS)',),
    SimpleTerm(u'DEBS', u'DEBS', u'Diethylbenzothiazolsulfenamid (DEBS)'),
    SimpleTerm(u'CBS', u'CBS', u'N-Cyclohexyl-2-benzothiazylsulfenamid (CBS)'),
    SimpleTerm(u'DCBS', u'DCBS', u'Dicyclohexylbenzothiazolsufenamid (DCBS)'),
    SimpleTerm(u'p-Phenylendiamin-Derivate', u'p-Phenylendiamin-Derivate' u'p-Phenylendiamin-Derivate'),
    SimpleTerm(u'IPPD', u'IPPD', u"N-Isopropyl-N'-phenyl-p-phenylendiamin (IPPD)"),
    SimpleTerm(u'DPPD', u'DPPD', u"N,N'-Diphenyl-p-phenylendiamin (DPPD)"),
    SimpleTerm(u'Mercaptobenzimidazol', u'Mercaptobenzimidazol', u'Mercaptobenzimidazol'),
    SimpleTerm(u'1,3-Diphenylguanidin', u'1,3-Diphenylguanidin', u'1,3-Diphenylguanidin'),
    SimpleTerm(u'Hydrochinon', u'Hydrochinon', u'Hydrochinon'),
    SimpleTerm(u'Hexamethylentetramin', u'Hexamethylentetramin', u'Hexamethylentetramin'),
    SimpleTerm(u'HN-Cyclohexylthiophthalimid', u'HN-Cyclohexylthiophthalimid', u'HN-Cyclohexylthiophthalimid'),
    SimpleTerm(u'Naturlatex', u'Naturlatex', u'Naturlatex'),
    SimpleTerm(u'Maisstaerke', u'Maisstaerke', u'Maisstärke'),
    ))

pruefung374neu = SimpleVocabulary((
    SimpleTerm(u'keine', u'keine', u'keine Prüfung'),
    SimpleTerm(u'TypA', u'TypA', u'EN ISO 374-1 / Typ A (6 Prüfchemikalien)'),
    SimpleTerm(u'TypB', u'TypB', u'EN ISO 374-1 / Typ B (3 Prüfchemikalien)'),
    SimpleTerm(u'TypC', u'TypC', u'EN ISO 374-1 / Typ C (1 Prüfchemikalie)'),
    ))

chemikalienpruefung = SimpleVocabulary((
    SimpleTerm(u'67-56-1', u'A', u'(A) Methanol'),
    SimpleTerm(u'67-64-1', u'B', u'(B) Aceton'),
    SimpleTerm(u'75-05-8', u'C', u'(C) Acetonitril'),
    SimpleTerm(u'75-09-2', u'D', u'(D) Dichlormethan'),
    SimpleTerm(u'75-15-0', u'E', u'(E) Schwefelkohlenstoff (Kohlenstoffdisulfid)'),
    SimpleTerm(u'108-88-3', u'F', u'(F) Tuluol'),
    SimpleTerm(u'109-89-7', u'G', u'(G) Diethylamin'),
    SimpleTerm(u'109-99-9', u'H', u'(H) Tetrahydrofuran'),
    SimpleTerm(u'141-78-6', u'I', u'(I) Essigsäureethylester (Ethylacetat)'),
    SimpleTerm(u'142-82-5', u'J', u'(J) n-Heptan'),
    SimpleTerm(u'1310-73-2', u'K', u'(K) Natriumhydroxid 40 %'),
    SimpleTerm(u'7664-93-9', u'L', u'(L) Schwefelsäure 96 %'),
    SimpleTerm(u'7697-37-2', u'M', u'(M) Salpetersäure 65 %'),
    SimpleTerm(u'64-19-7', u'N', u'(N) Essigsäure 99 %'),
    SimpleTerm(u'1336-21-6', u'O', u'(O) Ammoniak 25 %'),
    SimpleTerm(u'7722-84-1', u'P', u'(P) Wasserstoffperoxid 30%'),
    SimpleTerm(u'7664-39-3', u'S', u'(S) Flusssäure 40 %'),
    SimpleTerm(u'50-00-0', u'T', u'(T) Formaldehyd 37 %'),
    ))

pruefung375_5_2016 = SimpleVocabulary((
    SimpleTerm(u'keine', u'keine', u'keine Prüfung'),
    SimpleTerm(u'bakterienpilze', u'bakterienpilze', u'Schutz vor Bakterien und Pilzen'),
    SimpleTerm(u'bakterienpilzeviren', u'bakterienpilzeviren', u'Schutz vor Bakterien, Pilzen und Viren')
    ))

pruefung_weitere_chemie = SimpleVocabulary((
    SimpleTerm(u'din_en_16523', u'din_en_16523', u'DIN EN 16523'),
    ))

pruefung_normen_mechanik = SimpleVocabulary((
    SimpleTerm(u'din_en_381', u'din_en_381', u'DIN EN 381'),
    SimpleTerm(u'din_en_388_alt', u'din_en_388_alt', u'DIN EN 388 vor 2016'),
    SimpleTerm(u'din_en_388_2016', u'din_en_388_2016', u"EN 388:2016"),
    ))

catvalue1 = SimpleVocabulary.fromItems((
    ("x", "x"),
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4")))

catvalue2 = SimpleVocabulary.fromItems((
    ("x", "x"),
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5")))

catvalue3 = SimpleVocabulary.fromItems((
    ("x", "x"),
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    ("E", "E"),
    ("F", "F")))

catvalue4 = SimpleVocabulary.fromItems((
    ("x", "x"),
    ("P", "P")))

catvalue5 = SimpleVocabulary.fromItems((
    ("x", "x"),
    ("0", "0"),
    ("1", "1")))
