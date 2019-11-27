from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
# from nva.praeventionswissen.vocabularies import desinf_anwendung, desinf_produktgruppe, desinf_wirksamkeit, desinf_pruefung, einwirkzeit

# from bgetem.hautschutz import _


class IDesinfektionsmittel(model.Schema):
    """
    Schema eines Desinfektionsmittels
    """

    title = schema.TextLine(title=u"Produktname")

#    anwendungsbereich = schema.Choice(
#            title=u"Anwendungsbereich",
#            source=desinf_anwendung,
#            required=True,)

#    produktgruppe = schema.Choice

#    wirksamkeit = schema.List

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
