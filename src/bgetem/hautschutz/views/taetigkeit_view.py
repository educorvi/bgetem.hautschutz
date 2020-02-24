# -*- coding: utf-8 -*-

from bgetem.hautschutz import _
from Products.Five.browser import BrowserView
from bgetem.hautschutz.vocabularies import gefaehrdungen
from bgetem.hautschutz.vocabularies import rankvalue
from bgetem.hautschutz.vocabularies import biologische_gefaehrdung

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class TaetigkeitView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('taetigkeit_view.pt')

    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A small message')
        return self.index()

    def get_gefaehrdung(self):
        gefaehrdunge = u""
        if self.context.gefaehrdung:
            gefaehrdunge = gefaehrdungen.getTerm(self.context.gefaehrdung).title
        return gefaehrdunge

    def get_biologie(self):
        biologien = u""
        if self.context.biologie:
            biologien = biologische_gefaehrdung.getTerm(self.conrtext.biologie).title
        return biologien

    def get_mechanik(self):
        mechaniken = u""
        if self.context.mechanik:
            mechanikem = gefaehrdungen.getTerm(self.context.mechanik).title
        return mechaniken

    def get_abrieb(self):
        abriebe = u""
        if self.context.abrieb:
            abriebe = rankvalue.getTerm(self.context.abrieb).title
        return abriebe

    def get_schnitt(self):
        schnitte = u""
        if self.context.schnitt:
            schnitte = rankvalue.getTerm(self.context.schnitt).title
        return schnitte

    def get_riss(self):
        risse = u""
        if self.context.riss:
            risse = rankvalue.getTerm(self.context.riss).title
        return risse

    def get_stick(self):
        sticke = u""
        if self.context.stick:
            sticke = rankvalue.getTerm(self.context.stick).title
        return sticke

    def get_brennverhalten(self):
        brennverhalt = u""
        if self.context.brennverhalten:
            brennverhalt = rankvalue.getTerm(self.context.brennverhalten).title
        return brennverhalt

    def get_stoss(self):
        stosse = u""
        if self.context.stoss:
            stosse = rankvalue.getTerm(self.context.stoss).title
        return stosse

    def get_brennverhalten(self):
        brennverhalt = u""
        if self.context.brennverhalten:
            brennverhalt = rankvalue.getTerm(self.context.brennverhalten).title
        return brennverhalt

    def get_kontaktwaerme(self):
        kontaktwaermen = u""
        if self.context.kontaktwaerme:
            kontaktwaermen = rankvalue.getTerm(self.context.kontaktwaerme).title
        return kontaktwaermen

    def get_konvektivehitze(self):
        konvektivehitzen = u""
        if self.context.konvektive_hitze:
            konvektivehitzen = rankvalue.getTerm(self.context.konvektive_hitze).title
        return konvektivehitzen

    def get_strahlungswaerme(self):
        strahlungswaermen = u""
        if self.context.strahlungswaerme:
            strahlungswaermen = rankvalue.getTerm(self.context.strahlungswaerme).title
        return strahlungswaermen

    def get_metallspritzer(self):
        metallspritzern = u""
        if self.context.metallspritzer:
            metallspritzern = rankvalue.getTerm(self.context.metallspritzer).title
        return metallspritzern

    def get_fluessigesmetall(self):
        fluessigesmetalle = u""
        if self.context.fluessigesmetall:
            fluessigesmetalle = rankvalue.getTerm(self.context.fluessigesmetall).title
        return fluessigesmetalle

    def get_konvektivekaelte(self):
        konvektivekaelten = u""
        if self.context.konvektive_kaelte:
            konvektivekaelten = rankvalue.getTerm(self.context.konvektive_kaelte).title
        return konvektivekaelten

    def get_kontaktkaelte(self):
        kontaktkaelten = u""
        if self.context.kontaktkaelte:
            kontaktkaelten = rankvalue.getTerm(self.context.kontaktkaelte).title
        return kontaktkaelten

    def get_wasserdichtigkeit(self):
        wasserdichtigkeiten = u""
        if self.context.wasserdichtigkeit:
            wasserdichtigkeiten = rankvalue.getTerm(self.context.wasserdichtigkeit).title
        return wasserdichtigkeiten
