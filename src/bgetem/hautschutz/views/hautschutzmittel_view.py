# -*- coding: utf-8 -*-

from bgetem.hautschutz import _
from Products.Five.browser import BrowserView
from bgetem.hautschutz.vocabularies import hautschutzmittelanwendungen
from bgetem.hautschutz.vocabularies import hskategorieVocabulary
from bgetem.hautschutz.vocabularies import zusatzVocabulary

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class HautschutzmittelView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('hautschutzmittel_view.pt')

    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A small message')
        return self.index()

    def get_herstellerdaten(self):
        herstellerdaten = {}
        if self.context.hersteller:
            hersteller = self.context.hersteller.to_object
            herstellerdaten['name'] = hersteller.title
            herstellerdaten['anschrift1'] = hersteller.anschrift1
            herstellerdaten['anschrift2'] = hersteller.anschrift2
            herstellerdaten['anschrift3'] = hersteller.anschrift3
            herstellerdaten['telefon'] = hersteller.telefon
            herstellerdaten['email'] = hersteller.email
            herstellerdaten['homepage'] = hersteller.homepage
        return herstellerdaten

    def producktname(self):
        title = self.context.title
        return title

    def gefaehrdung(self):
        gefaehrdung = self.context.gefaehrdung
        return gefaehrdung

    def get_gefaehrdung(self):
        gefaehrdungen = []
        for i in self.context.gefaehrdung:
            gefaehrdungen.append(hautschutzmittelanwendungen.getTerm(i).title)
        return gefaehrdungen

    def kategorie(self):
        kategorie = self.context.kategorie
        return kategorie

    def get_kategorie(self):
        kategorien = []
        for i in self.context.kategorie:
            kategorien.append(hskategorieVocabulary.getTerm(i).title)
        return kategorien

    def uvschutzfaktor(self):
        uvschutzfaktor = self.context.uvschutzfaktor
        return uvschutzfaktor

    def schweissrauche(self):
        schweissrauche = self.context.schweissrauche
        return schweissrauche

    def zusatzfunktion(self):
        zusatzfunktion = self.context.zusatzfunktion
        return zusatzfunktion

    #def get_zusatzfunktion(self):
        #zusatzfunktionen = []
        #for i in self.context.zusatzfunktion:
            #zusatzfunktionen.append(zusatzVocabulary.getTerm(i).title)
        #return zusatzfunktionen

    def inhaltsstoffe(self):
        inhaltsstoffe = self.context.inhaltsstoffe
        return inhaltsstoffe

    def konservierungsmittel(self):
        konservierungsmittel = self.context.konservierungsmittel
        return konservierungsmittel

    def duftstoffe(self):
        duftstoffe = self.context.duftstoffe
        return duftstoffe

    def bemerkungen(self):
        bemerkungen = self.context.bemerkungen
        return bemerkungen
