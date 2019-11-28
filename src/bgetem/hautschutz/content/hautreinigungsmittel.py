# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer


# from bgetem.hautschutz import _


class IHautreinigungsmittel(model.Schema):
    """ 
    Schema eines Hautreinigungsmittels
    """

    title = schema.TextLine(title=u"Produktname")

#    anwendungsbereich = schema.List(title=u"Anwendungsbereich", value_type=schema.Choice(vocabulary=schmutzVocabulary), required=False,)

    inhaltsstoffe = schema.List(title=u"Inhaltsstoffe", value_type=schema.TextLine(), required=False)

    reibemittel = schema.List(title=u"Reibemittel", value_type=schema.TextLine(), required=False)

    loesemittel = schema.List(title=u"Lösemittel", value_type=schema.TextLine(), required=False)

    konservierungsmittel = schema.List(title=u"Konservierungsmittel", value_type=schema.TextLine(), required=False)

    duftstoffe = schema.List(title=u"Duftstoffe", value_type=schema.TextLine(), required=False)

    bemerkungen = schema.Text(title=u"Bemerkungen", required=False)

#    bild = NamedBlobImage(title=u"Produktbild", required=False)

 #   hersteller = RelationChoice(
 #       title=u"Hersteller oder Lieferant",
 #       source=ObjPathSourceBinder(),
 #       required=False,)



@implementer(IHautreinigungsmittel)
class Hautreinigungsmittel(Container):
    """
    """
