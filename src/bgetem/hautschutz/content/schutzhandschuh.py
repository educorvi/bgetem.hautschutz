# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer

from bgetem.hautschutz.vocabularies import material, pruefung374alt, profilierung, cecatvalues, allergene_vocab, pruefung374neu, chemikalienpruefung, pruefung375_5_2016, pruefung_weitere_chemie, pruefung_normen_mechanik

from bgetem.hautschutz.vocabularies import catvalue1, catvalue2, catvalue3, catvalue4, catvalue5
from plone.namedfile.field import NamedBlobImage

from z3c.relationfield.schema import RelationChoice
from plone.app.vocabularies.catalog import CatalogSource

from bgetem.hautschutz import _

from plone.autoform import directives #as form

from z3c.form.browser.checkbox import CheckBoxFieldWidget
from z3c.form.browser.radio import RadioFieldWidget

#from collective.z3cform.datagridfield import DataGridFieldFactory
#from collective.z3cform.datagridfield import DictRow

class ISchutzhandschuh(model.Schema):
    """
    Schema eines Schutzhandschuhs
    """

    title = schema.TextLine(title=_(u"Produktname"))

    text = RichText(title=_(u"Weitere Beschreibungen des Produkts"), required = False)

    bild = NamedBlobImage(title=_(u"Produktbild"), required=False)

    hersteller = RelationChoice(
        title=_(u"Hersteller oder Lieferant"),
        source=CatalogSource(portal_type=["Folder", "Hersteller"]),
        required=False)

    directives.widget('material_aussen', CheckBoxFieldWidget)
    material_aussen = schema.List(title=_(u"Material außen"), value_type=schema.Choice(vocabulary=material), required=False,)

    directives.widget('material_innen', CheckBoxFieldWidget)
    material_innen = schema.List(title=_(u"Material innen"), value_type=schema.Choice(vocabulary=material), required=False)

    directives.widget('profilierung', CheckBoxFieldWidget)
    profilierung = schema.List(title=_(u"Profilierung"), value_type=schema.Choice(vocabulary=profilierung), required=False)

    schichtstaerke_min = schema.Float(title=_(u"Schichtstärke (min) in mm"), required=False)
    schichtstaerke_max = schema.Float(title=_(u"Schichtstärke (max) in mm"), required=False)

    gesamtlaenge_von = schema.Int(title=_(u"Gesamtlänge (von) in mm"), required=False)
    gesamtlaenge_bis = schema.Int(title=_(u"Gesamtlänge (bis) in mm"), required=False)

    cecategory = schema.Choice(title=_(u"CE-Kategorie"), vocabulary=cecatvalues)

    allergene = schema.List(title=_(u"Allergene"), value_type=schema.Choice(vocabulary=allergene_vocab), required=False)

    esd = schema.Bool(title=_(u"ESD Produktschutz"))

    model.fieldset(
        'biologie',
        label=u"Biologische Risiken",
        #fields=['norm374_2003', 'norm374_2016', 'chemikalienliste', 'norm374_5', 'gefahrstoffschutz']
        fields=['norm374_5',]
    )

    model.fieldset(
        'chemie',
        label=u"Chemische Risiken",
        #fields=['norm374_2003', 'norm374_2016', 'chemikalienliste', 'norm374_5', 'gefahrstoffschutz']
        fields=['norm374_2003', 'norm374_2016', 'chemikalienliste', 'chemie_weitere']
    )

    directives.widget('norm374_2003', CheckBoxFieldWidget)
    norm374_2003 = schema.List(title=_(u"Norm EN 374-1:2003 (3 Prüfchemikalien)"),
                               value_type=schema.Choice(vocabulary=pruefung374alt),
                               required=False)

    directives.widget('norm374_2016', RadioFieldWidget)
    norm374_2016 = schema.Choice(title=_(u"Norm EN ISO 374-1:2016"),
                                 vocabulary=pruefung374neu,
                                 default='keine',
                                 required=False)

#    directives.widget('chemikalienliste', CheckBoxFieldWidget)
    chemikalienliste = schema.List(title=_(u"Liste der Prüfchemikalien"),
                                    description=_(u"Bitte wählen Sie aus, welche Chemikalien bei der Permeationsprüfung verwendet wurden."),
                                    value_type=schema.Choice(vocabulary=chemikalienpruefung),
                                    required=False)

    directives.widget('norm374_5', RadioFieldWidget)
    norm374_5 = schema.Choice(title=_(u"Norm EN ISO 374-5:2016"),
                              description=_(u"Schutz gegen Mikroorganismen"),
                              vocabulary=pruefung375_5_2016,
                              default='keine',
                              required=False)

    directives.widget('chemie_weitere', CheckBoxFieldWidget)
    chemie_weitere = schema.List(title=_(u"Prüfung gegen weitere Normen"),
                                 description=_(u"Bitte wählen Sie aus, gegen welche Normen das Produkt außerdem geprüft wurde."),
                                 value_type=schema.Choice(vocabulary=pruefung_weitere_chemie),
                                 required=False,)

#    directives.widget('gefahrstoffschutz', DataGridFieldFactory)
#    form.omitted(IEditForm, 'gefahrstoffschutz')
#    gefahrstoffschutz = schema.List(title=_(u'Gefahrstoffschutz für dieses Produkt.'),
#                        value_type=DictRow(title=_(u"Gefahrstoff"), schema=IGefahrstoffe),
#                        required = False,)

    model.fieldset(
        'mechanik',
        label=u"Mechanische Risiken",
        fields=['mechanik', 'abrieb', 'schnittcoup', 'riss', 'stick', 'schnittiso', 'stoss']
    )

    directives.widget('mechanik', CheckBoxFieldWidget)
    mechanik = schema.List(title=_(u"Prüfung gegen Normen der mechanischen Beständigkeit"),
                           description=_(u"Bitte wählen Sie aus, gegen welche Normen der Handschuh geprüft wurde."),
                           value_type=schema.Choice(vocabulary=pruefung_normen_mechanik),
                           required=False)

    abrieb = schema.Choice(title=u"Abriebfestigkeit", vocabulary=catvalue1, required=False)
    schnittcoup = schema.Choice(title=u"Schnittfestigkeit (Coup-Test)", vocabulary=catvalue2, required=False)
    riss = schema.Choice(title=u"Weiterreißfestigkeit", vocabulary=catvalue1, required=False)
    stick = schema.Choice(title=u"Durchstichfestigkeit", vocabulary=catvalue1, required=False)
    schnittiso = schema.Choice(title=u"Schnittfestigkeit (ISO)", vocabulary=catvalue3, required=False)
    stoss = schema.Choice(title=u"Schutz gegen Stosseinwirkung", vocabulary=catvalue4, required=False)

    model.fieldset(
        'hitze',
        label=u"Hitze",
        fields = ['en407', 'brennverhalten', 'kontaktwaerme', 'konvektive_hitze', 'strahlungswaerme',
                  'metallspritzer','fluessigesmetall']
    )

    model.fieldset(
        'kaelte',
        label=u"Kälte",
        fields = ['en511', 'konvektive_kaelte', 'kontaktkaelte', 'wasserdichtigkeit']
    )

    en407 = schema.Bool(title=_(u"Norm 407"),
                      description=_(u"Erfüllt der Schutzhandschuh die Norm 407 bzw. wurde er dagegen getestet?"),)
    brennverhalten = schema.Choice(title=u"Brennverhalten", vocabulary=catvalue1, required=False)
    kontaktwaerme = schema.Choice(title=u"Kontaktwärme", vocabulary=catvalue1, required=False)
    konvektive_hitze = schema.Choice(title=u"Konvektive Hitze", vocabulary=catvalue1, required=False)
    strahlungswaerme = schema.Choice(title=u"Strahlungswärme", vocabulary=catvalue1, required=False)
    metallspritzer = schema.Choice(title=u"Belastung durch kleine Spritzer geschmolzenen Metalls",
                               vocabulary=catvalue1, required=False)
    fluessigesmetall = schema.Choice(title=u"Belastung durch große Mengen flüssigen Metalls",
                          vocabulary=catvalue1, required=False)
    en511 = schema.Bool(title=_(u"Norm 511"),
                        description=_(u"Erfüllt der Schutzhandschuh die Norm 511 bzw. wurde er dagegen getestet?"),)
    konvektive_kaelte = schema.Choice(title=u"Konvektive Kälte", vocabulary=catvalue1, required=False)
    kontaktkaelte = schema.Choice(title=u"Kontaktkälte", vocabulary=catvalue1, required=False)
    wasserdichtigkeit = schema.Choice(title=u"Wasserdichtigkeit", vocabulary=catvalue5, required=False)

    model.fieldset(
        'elektrisch',
        label=_(u"Elektrische Risiken"),
        fields=['dummy_elektrisch'],
    )

    dummy_elektrisch = schema.TextLine(title=u"Dummy-Feld Norm",
                            description=u"Bereich für die Felder aus dem Bereich Elektrische Gefährdungen", required=False)

    model.fieldset(
        'schweisser',
        label=_(u"Schweisser Schutzhandschuh"),
        fields=['dummy_schweisser'],
    )

    dummy_schweisser = schema.TextLine(title=u"Dummy-Feld Norm",
                            description=u"Bereich für die Felder aus dem Bereich Schweisser Schutzhandschuhe", required=False)




@implementer(ISchutzhandschuh)
class Schutzhandschuh(Container):
    """
    Das ist die Klasse fuer den Schutzhandschuh.
    """
