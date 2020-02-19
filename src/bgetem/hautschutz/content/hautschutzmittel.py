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
from bgetem.hautschutz.vocabularies import hautschutzmittelanwendungen, hskategorieVocabulary, zusatzVocabulary
from plone.namedfile.field import NamedBlobImage

from bgetem.hautschutz import _

class IHautschutzmittel(model.Schema):
    """
    Schema eines Hautschutzmittels
    """

    title = schema.TextLine(title=_(u"Produktname"))

    gefaehrdung = schema.List(title=_(u'Gefährdung'), value_type=schema.Choice(vocabulary=hautschutzmittelanwendungen, required=False), required=False)

    kategorie = schema.List(title=_(u'Schutzfunktion bei chemischer Gefährdung'), value_type=schema.Choice(vocabulary=hskategorieVocabulary), required=False)

    uvschutzfaktor = schema.TextLine(title=_(u'Sonnenschutzfaktor'), required=False)

    schweissrauche = schema.TextLine(title=_(u'Zusatzangaben bei Schweissarbeiten'), required=False)

    zusatzfunktion = schema.Choice(title=_(u'Zusatzfunktion'), vocabulary=zusatzVocabulary, default="keine", required=False)

    inhaltsstoffe = schema.List(title=_(u'Inhaltsstoffe'), value_type=schema.TextLine(), required=False)

    konservierungsmittel = schema.List(title=_(u"Konservierungsmittel"), value_type=schema.TextLine(), required=False)

    duftstoffe = schema.List(title=_(u"Duftstoffe"), value_type=schema.TextLine(), required=False)

    bemerkungen = schema.Text(title=_(u"Bemerkungen"), required=False)

    bild = NamedBlobImage(title=_(u'Produktbild'), required=False)



@implementer(IHautschutzmittel)
class Hautschutzmittel(Container):
    """
    """
