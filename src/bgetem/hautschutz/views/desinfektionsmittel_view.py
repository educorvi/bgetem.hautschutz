# -*- coding: utf-8 -*-

from bgetem.hautschutz import _
from Products.Five.browser import BrowserView
from bgetem.hautschutz.vocabularies import desinf_wirksamkeit
from bgetem.hautschutz.vocabularies import desinf_anwendung
from bgetem.hautschutz.vocabularies import desinf_produktgruppe
# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class DesinfektionsmittelView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('desinfektionsmittel_view.pt')

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

    def anwendungsbereich(self):
        anwendungsbereich = self.context.anwendungsbereich
        return anwendungsbereich

    def get_anwendung(self):
        anwendungen = u""
        if self.context.anwendungsbereich:
            anwendungen = desinf_anwendung.getTerm(self.context.anwendungsbereich).title
        return anwendungen

    def produktgruppe(self):
        produktgruppe = self.context.produktgruppe
        return produktgruppe

    def get_produktgruppe(self):
        produktgruppen = []
        if self.context.produktgruppe:
            produktgruppen = desinf_produktgruppe.getTerm(self.context.produktgruppe).title
        return produktgruppen


    def wirksamkeit(self):
        wirksamkeit = self.context.wirksamkeit
        return wirksamkeit

    def get_wirksamkeit(self):
        wirksamkeiten = []
        for i in self.context.wirksamkeit:
            wirksamkeiten.append(desinf_wirksamkeit.getTerm(i).title)
        return wirksamkeiten

    def einwirkung(self):
        einwirkung = self.context.einwirkung
        return einwirkung

    def pruefung(self):
        pruefung = self.context.pruefung
        return pruefung

    def bemerkungen(self):
        bemerkungen = self.context.bemerkungen
        return bemerkungen

