from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from bgetem.hautschutz.vocabularies import desinf_anwendung, desinf_produktgruppe, desinf_wirksamkeit

from bgetem.hautschutz import _


class IDesinfektionsmittel(model.Schema):
    """
    Schema eines Desinfektionsmittels
    """

    title = schema.TextLine(title=_(u"Produktname"))

    anwendungsbereich = schema.Choice(
            title=_(u"Anwendungsbereich"),
            source=desinf_anwendung,
            required=True,)

    produktgruppe = schema.Choice(
            title=_(u"Produktgruppe"),
            source=desinf_produktgruppe,
            default=u'haendedesinketionsmittel',
            required=True,
    )
    
    wirksamkeit = schema.List(
            title=_(u"Wirksamkeit"),
            value_type=schema.Choice(
                source=desinf_wirksamkeit,),
            required=True,
    )

#    einwirkung = schema.Choice

#    pruefung = schema.Choice

    bemerkungen = schema.Text(title=u"Bemerkungen", required=False)

#    bild = NamedBlobImage(title=u"Produktbild", required=False)

#    hersteller = RelationChoice(
#            title=u"Hersteller oder Lieferant",
#            source=ObjPathSourceBinder(),
#            required=False,
#            )




@implementer(IDesinfektionsmittel)
class Desinfektionsmittel(Container):
    """
    """
