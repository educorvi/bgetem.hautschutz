# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer


# from bgetem.hautschutz import _


class ISchutzhandschuh(model.Schema):
    """ 
    Schema eines Schutzhandschuhs
    """

    title = schema.TextLine(title=u"Produktname")

    text = RichText(title=u"Weitere Beschreibungen des Produkts", required = False)

    bild = NamedBlobImage(title=u"Produktbild", required=False)

    hersteller = RelationChoice(
            title=u"Hersteller oder Lieferant",
            source=ObjPathSourceBinder(),
            required=False,
            )

    form.widget(material_aussen=CheckBoxFieldWidget)
    material_aussen = schema.List(title=u"Material außen", value_type=schema.Choice(vocabulary=material), required=False,)

    form.widget(material_innen=CheckBoxFieldWidget)
    material_innen = schema.List(title=u"Material innen", value_type=schema.Choice(vocabulary=material), required=False)

    form.widget(profilierung=CheckBoxFieldWidget)
    profilierung = schema.List(tiel=u"Profilierung", value_type=schema.Choice(vocabulary=profilierung), required=False)

    schichtstaerke_min = schema.Float(title=u"Schichtstärke (min) in mm", required=False)
    schichtstaerke_max = schema.Float(title=u"Schichtstärke (max) in mm", required=False)

    gesamtlaenge_von = schema.Int(title=u"Gesamtlänge (von) in mm", required=False)
    gesamtlaenge_bis = schema.Int(title=u"Gesamtlänge (bis) in mm", requierd=False)

    cecategory = schema.Choice(title=u"CE-Kategorie", vocabulary=cecatcalues)

    allergene = schema.List(title=u"Allergene", value_type=schema.Choice(vocabulary=allergene_vocab), required=False)

    m1.fieldset(
            'chemie',
            label=u"Chemische/Biologische Risiken",
            fields=['norm374_2003', 'norm374_2016', 'chemikalienliste', 'norm374_5', 'gefahrstoffschutz']
    )



@implementer(ISchutzhandschuh)
class Schutzhandschuh(Container):
    """
    Das ist die Klasse fuer den Schutzhandschuh.
    """
