from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from bgetem.hautschutz.vocabularies import desinf_anwendung, desinf_produktgruppe, desinf_wirksamkeit, einwirkzeit, desinf_pruefung

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

    einwirkung = schema.Choice(
            title = _(u"Einwirkzeit"),
            source = einwirkzeit,
            required = True,
    )

    pruefung = schema.Choice(
            title=_(u"Wirksamkeit geprüft und gelistet von:"),
            source=desinf_pruefung,
            default=u'vah',
            required=True,
    )

    bemerkungen = schema.Text(title=_(u"Bemerkungen"), required=False)


#    hersteller = RelationChoice(
#            title=u"Hersteller oder Lieferant",
#            source=ObjPathSourceBinder(),
#            required=False,
#            )




@implementer(IDesinfektionsmittel)
class Desinfektionsmittel(Container):
    """
    """
