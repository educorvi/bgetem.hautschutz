from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer


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

@implementer(IDesinfektionsmittel)
class Desinfektionsmittel(Container):
    """
    """
