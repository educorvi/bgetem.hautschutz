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


from bgetem.hautschutz import _

from bgetem.hautschutz.vocabularies import gefaehrdungen, rankvalue, biologische_gefaehrdung

class ITaetigkeit(model.Schema):
    """ Marker interface and Dexterity Python Schema for Taetigkeit
    """

    title = schema.TextLine(title=_(u"Tätigkeit"))

    description=schema.TextLine(title=_(u"Kurzbeschreibung"), required=False)

    text = schema.Text(title=_(u"Weitere Beschreibungungen der Tätigkeit"), required=False)

    gefaehrdung = schema.Choice(title=_(u"Primäre Gefährdung bei dieser Tätigkeit"),
        description=_(u"Bitte wählen Sie hier die primäre Gefährdung bei dieser Tätigkeit aus."),
        source = gefaehrdungen,
        required = True,
    )

#    model.fieldset(
#        'chemie',
#        label=_(u"Chemische/Biologische Risiken"),
#        fields=['gefahrstoffschutz', 'biologie']
#        fields=['gefahrstoffschutz']
#    )

#    directives.widget('gefahrstoffschutz', DataGridFieldFactory)
#    gefahrstoffschutz = schema.List(title = u'Gefahrstoffkontakt bei dieser Tätigkeit',
#                        value_type=DictRow(title=u"Gefahrstoff", schema=IGefahrstoffe),
#                        required = False,)

    biologie = schema.Choice(title=_(u"Mit folgenden biologischen Gefährdungen ist diese Tätigkeit verbunden:"),
                      source=biologische_gefaehrdung, required=True)


    model.fieldset(
        'mechanik',
        label=_(u"Mechanische Risiken"),
        fields=['mechanik', 'kettensaege', 'abrieb', 'schnitt', 'riss', 'stick', 'stoss']
    )

    mechanik = schema.Bool(title=_(u"Mechanische Gefährdungen"),
                           description=_(u"(Beispiel: Arbeit mit spitzen oder scharfkantigen Gegenstände, Stosseinwirkung)"),
                           required=False)

    kettensaege = schema.Bool(title=_(u"Arbeit mit handgeführten Kettensägen"), required=False)
    abrieb = schema.Choice(title=_(u"Anforderung an Abriebfestigkeit"), vocabulary=rankvalue, default='nicht_relevant', required=False)
    schnitt = schema.Choice(title=_(u"Anforderung an Schnittfestigkeit"), vocabulary=rankvalue, default='nicht_relevant', required=False)
    riss = schema.Choice(title=_(u"Anforderung an Weiterreißfestigkeit"), vocabulary=rankvalue, default='nicht_relevant', required=False)
    stick = schema.Choice(title=_(u"Anforderung an Durchstichfestigkeit"), vocabulary=rankvalue, default='nicht_relevant', required=False)
    stoss = schema.Choice(title=_(u"Anforderung an Schutz gegen Stosseinwirkung"), vocabulary=rankvalue, default='nicht_relevant', required=False)

    model.fieldset(
        'waerme_kaelte',
        label=_(u"Wärme / Kälte"),
        fields = ['thermisch', 'brennverhalten', 'kontaktwaerme', 'konvektive_hitze', 'strahlungswaerme',
                  'metallspritzer','fluessigesmetall', 'konvektive_kaelte', 'kontaktkaelte',
                  'wasserdichtigkeit'],
    )

    thermisch = schema.Bool(title=_(u"Thermische Gefährdungen"),
                      description=_(u"(Hitze oder Kälteeinwirkung)"),
                      required=False)

    brennverhalten = schema.Choice(title=_(u"Anforderung an das Brennverhalten"), vocabulary=rankvalue, default='nicht_relevant', required=False)
    kontaktwaerme = schema.Choice(title=_(u"Anforderung an die Kontaktwärme"), vocabulary=rankvalue, default='nicht_relevant', required=False)
    konvektive_hitze = schema.Choice(title=_(u"Anforderung an die Konvektive Hitze"), vocabulary=rankvalue, default='nicht_relevant', required=False)
    strahlungswaerme = schema.Choice(title=_(u"Anforderung an die Strahlungswärme"), vocabulary=rankvalue, default='nicht_relevant', required=False)
    metallspritzer = schema.Choice(title=_(u"Anforderung an die Belastung durch kleine Spritzer geschmolzenen Metalls"),
                               vocabulary=rankvalue, default='nicht_relevant', required=False)
    fluessigesmetall = schema.Choice(title=_(u"Anforderung an die Belastung durch große Mengen flüssigen Metalls"),
                          vocabulary=rankvalue, default='nicht_relevant', required=False)

    konvektive_kaelte = schema.Choice(title=_(u"Anforderung an die Konvektive Kälte"), vocabulary=rankvalue, default='nicht_relevant', required=False)
    kontaktkaelte = schema.Choice(title=_(u"Anforderung an die Kontaktkälte"), vocabulary=rankvalue, default='nicht_relevant', required=False)
    wasserdichtigkeit = schema.Choice(title=_(u"Anforderung an die Wasserdichtigkeit"), vocabulary=rankvalue, default='nicht_relevant', required=False)



@implementer(ITaetigkeit)
class Taetigkeit(Container):
    """
    """
