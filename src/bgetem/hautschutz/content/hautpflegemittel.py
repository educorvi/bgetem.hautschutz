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
from bgetem.hautschutz.vocabularies import anwendungVocabulary

from bgetem.hautschutz import _


class IHautpflegemittel(model.Schema):
    """ Marker interface and Dexterity Python Schema for Hautpflegemittel
    """

    title = schema.TextLine(title=_(u"Produktname"))

    anwendungsbereich = schema.List(title=_(u"Anwendungsbereich"), value_type=schema.Choice(vocabulary=anwendungVocabulary), required=False,)

    inhaltsstoffe = schema.List(title=_(u"Inhaltsstoffe"), value_type=schema.TextLine(), required=False)

    konservierungsmittel = schema.List(title=u"Konservierungsmittel", value_type=schema.TextLine(), required=False)

    duftstoffe = schema.List(title=u"Duftstoffe", value_type=schema.TextLine(), required=False)

    bemerkungen = schema.Text(title=u"Bemerkungen", required=False)

#    bild = NamedBlobImage(title=u"Produktbild", required=False)

#    hersteller = RelationChoice(
#        title=u"Hersteller oder Lieferant",
#        source=ObjPathSourceBinder(),
#        required=False,
#        )


@implementer(IHautpflegemittel)
class Hautpflegemittel(Container):
    """
    """
