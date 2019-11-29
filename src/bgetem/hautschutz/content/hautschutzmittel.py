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

#from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

# from bgetem.hautschutz import _

#anwendungen = [
#        SimpleTerm(u"id_chemisch", u"id_chemisch", u"chemisch"),
#        SimpleTerm(u"id_biologisch", u"id_biologisch", u"biologisch"),
#        SimpleTerm(u"id_rauche", u"id_rauche", u"Schweissrauche"),
#        SimpleTerm(u"id_uvstrahlen", u"id_uvstrahlen", u"UV-Strahlen"),
#        ]

#anwendungVocabulary = SimpleVocabulary(anwendungen)

#zusatzVocabulary = SimpleVocabulary.fromItems((
#    (u"gegen Hauterweichung", "id_hauterweichung"),
#    (u"keine", "keine")))


class IHautschutzmittel(model.Schema):
    """
    Schema eines Hautschutzmittels
    """
    
    title = schema.TextLine(title=u"Produktname")

#    gefaehrdung = schema.List(title=u'Gefährdung', value_type=schema.Choice(vocabulary=anwendungVocabulary, required=False), required=False)

    uvschutzfaktor = schema.TextLine(title=u'Sonnenschutzfaktor', required=False)

    schweissrauche = schema.TextLine(title=u'Zusatzangaben bei SChweissarbeiten', required=False)

#    zusatzfunktion = schema.Choice(title==u'Zusatzfunktion', vocabulary=zusatzVocabulary, default="keine", required=False)

#    inhaltsstoffe = schema.List(title=u'Inhaltsstoffe', value_type=schema.TextLine(), required=False)

#    konservierungsmittel = schema.List(title=u"Konservierungsmittel", value_type=schema.TextLine(), required=False)

#    duftstoffe = schema.List(title=u"Duftstoffe", value_type=schema.TextLine(), required=Falase)

    bemerkungen = schema.Text(title=u"Bemerkungen", required=False)

#    bild NamedBlobImage(title=u'Produktbild', required=False)


@implementer(IHautschutzmittel)
class Hautschutzmittel(Container):
    """
    """
