# -*- coding: utf-8 -*-

from bgetem.hautschutz import _
from Products.Five.browser import BrowserView

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

    def kategorie(self):
        kategorie = self.cintext.kategorie
        return kategorie

    def uvschutzfaktor(self):
        uvschutzfaktor = self.cintext.uvschutzfaktor
        return uvschutzfaktor

    def schweissrauche(self):
        schweissrauche = self.context.schweissrauche
        return schweissrauche

    def zusatzfunktion(self):
        zusatzfunktion = self.context.zusatzfunktion
        return zusatzfunktion

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
