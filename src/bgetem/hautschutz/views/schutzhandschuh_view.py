# -*- coding: utf-8 -*-

from bgetem.hautschutz import _
from Products.Five.browser import BrowserView
from bgetem.hautschutz.vocabularies import material
from bgetem.hautschutz.vocabularies import profilierung

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SchutzhandschuhView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('schutzhandschuh_view.pt')

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

    def get_material_aussen(self):
        materialienaussen = []
        for i in self.context.material_aussen:
            materialien.append(material.getTrem(i).title)
        return materialienaussen

    def get_material_innen(self):
        materialieninnen = []
        for i in self.context.material_aussen:
            materialien.append(material.getTrem(i).title)
        return materialieninnen

    def get_profilierung(self):
        profilierungen = []
        for i in self.context.profilierung:
            profilierungen.append(profilierung.getTerm(i).title)
        return profilierungen
