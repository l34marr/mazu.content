from five import grok
from plone.directives import dexterity, form
from plone.indexer import indexer

from zope import schema
from plone.app.textfield import RichText

from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

from mazu.content import MessageFactory as _


class ITemple(form.Schema):
    """Temple Interface Class to Define Content-Type Schema
    """

    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/temple.xml to define the content type
    # and add directives here as necessary.

    #form.model("models/temple.xml")

    title = schema.TextLine(
        title=_(u"Title"),
    )

    data_src = schema.Choice(
        title=_(u"Data Source"),
        vocabulary='data_src',
        required=False,
    )

    position = schema.Choice(
        title=_(u"Position Type"), #Coordinate Type
        vocabulary='position',
        required=False,
    )

    facing = schema.TextLine(
        title=_(u"Sitting Facing"),
        required=False,
    )

    deity_main = schema.List(
        title=_(u"Deity Main"),
        value_type=schema.TextLine(),
        required=False,
    )

    deity_sub = schema.List(
        title=_(u"Deity Subsidiary"),
        value_type=schema.TextLine(),
        required=False,
    )

    religion = schema.Choice(
        title=_(u"Religion Type"),
        vocabulary='religion',
        required=False,
    )

    building = schema.Choice(
        title=_(u"Building Type"),
        vocabulary='building',
        required=False,
    )

    building_o = schema.TextLine(
        title=_(u"Building Type Other"),
        required=False,
    )

    registered = schema.TextLine(
        title=_(u"Registered Name"),
        description=_(u"Registry by Ministry of the Interior."),
        required=False,
    )

    funding = schema.Choice(
        title=_(u"Funding Type"),
        vocabulary='funding',
        required=False,
    )

    funding_o = schema.TextLine(
        title=_(u"Funding Type Other"),
        required=False,
    )

    organizing = schema.Choice(
        title=_(u"Organizing Type"),
        vocabulary='organizing',
        required=False,
    )

    organizing_o = schema.TextLine(
        title=_(u"Organizing Type Other"),
        required=False,
    )

    address = schema.TextLine(
        title=_(u"Address"),
        required=False,
    )

    in_charge = schema.TextLine(
        title=_(u"Person In Charge"),
        required=False,
    )

    tel = schema.TextLine(
        title=_(u"Telephone"),
        required=False,
    )

    homepage = schema.TextLine(
        title=_(u"Homepage"),
        required=False,
    )

    era = schema.TextLine(
        title=_(u"Common Era"),
        required=False,
    )

    year_accuracy = schema.Choice(
        title=_(u"Year Accuracy"),
        vocabulary='accrcy_y',
        required=False,
    )

    history = RichText(
        title=_(u"Establishment History"),
        required=False,
        default_mime_type='text/html',
        output_mime_type='text/html',
        allowed_mime_types=('text/html','text/plain',),
    )

    era_1 = schema.TextLine(
        title=_(u"Established Year by Taiwan Temple Collection"),
        required=False,
    )

    era_2 = schema.TextLine(
        title=_(u"Established Year by Taiwan Temple Overview"),
        required=False,
    )

    era_ref = RichText(
        title=_(u"References on Establishment"),
        required=False,
        default_mime_type='text/html',
        output_mime_type='text/html',
        allowed_mime_types=('text/html','text/plain',),
    )

    deity_accompany = RichText(
        title=_(u"Deities Accompany"),
        required=False,
        default_mime_type='text/html',
        output_mime_type='text/html',
        allowed_mime_types=('text/html','text/plain',),
    )

    worship = RichText(
        title=_(u"Worship"),
        required=False,
        default_mime_type='text/html',
        output_mime_type='text/html',
        allowed_mime_types=('text/html','text/plain',),
    )

    introduction = RichText(
        title=_(u"Introduction"),
        required=False,
        default_mime_type='text/html',
        output_mime_type='text/html',
        allowed_mime_types=('text/html','text/plain',),
    )

    overview = RichText(
        title=_(u"Building Overview"),
        required=False,
        default_mime_type='text/html',
        output_mime_type='text/html',
        allowed_mime_types=('text/html','text/plain',),
    )

    antiquity = RichText(
        title=_(u"Antiquities"),
        required=False,
        default_mime_type='text/html',
        output_mime_type='text/html',
        allowed_mime_types=('text/html','text/plain',),
    )

    narrate = RichText(
        title=_(u"Narrate"),
        required=False,
        default_mime_type='text/html',
        output_mime_type='text/html',
        allowed_mime_types=('text/html','text/plain',),
    )

    non_narrate = RichText(
        title=_(u"Non Narrate"),
        required=False,
        default_mime_type='text/html',
        output_mime_type='text/html',
        allowed_mime_types=('text/html','text/plain',),
    )

    academic = RichText(
        title=_(u"Academic Works"),
        required=False,
        default_mime_type='text/html',
        output_mime_type='text/html',
        allowed_mime_types=('text/html','text/plain',),
    )

    literature = RichText(
        title=_(u"Literature Reference"),
        required=False,
        default_mime_type='text/html',
        output_mime_type='text/html',
        allowed_mime_types=('text/html','text/plain',),
    )

    fill_in = schema.TextLine(
        title=_(u"Filling Person"),
        required=False,
    )

    fill_date = schema.TextLine(
        title=_(u"Filling Date"),
        required=False,
    )

    jstq = schema.TextLine(
        title=_(u"JiSiZuQun"),
        required=False,
    )

    jstq_o = schema.TextLine(
        title=_(u"JiSiZuQun Other"),
        required=False,
    )

    jsfw = RichText(
        title=_(u"JiSiFanWei"),
        required=False,
        default_mime_type='text/html',
        output_mime_type='text/html',
        allowed_mime_types=('text/html','text/plain',),
    )

    xyfw = RichText(
        title=_(u"XinYangFanWei"),
        required=False,
        default_mime_type='text/html',
        output_mime_type='text/html',
        allowed_mime_types=('text/html','text/plain',),
    )

    flxt = schema.TextLine(
        title=_(u"FenLingXiTong"),
        required=False,
    )

    flxt_o = schema.TextLine(
        title=_(u"FenLingXiTong Other"),
        required=False,
    )

    ymmy = schema.TextLine(
        title=_(u"YiMingMiaoYu"),
        required=False,
    )

    ymmy_o = schema.TextLine(
        title=_(u"YiMingMiaoYu Other"),
        required=False,
    )

    xhly = schema.TextLine(
        title=_(u"XiangHuoLaiYuan"),
        required=False,
    )

    xhly_o = schema.TextLine(
        title=_(u"XiangHuoLaiYuan Other"),
        required=False,
    )

    nlqs = schema.TextLine(
        title=_(u"NianLiQingSheng"),
        required=False,
    )

    nlqs_o = schema.TextLine(
        title=_(u"NianLiQingSheng Other"),
        required=False,
    )

    wyxx = schema.TextLine(
        title=_(u"WangYeXianXiang"),
        required=False,
    )

    wyxx_o = schema.TextLine(
        title=_(u"WangYeXianXiang Other"),
        required=False,
    )

    medicine = schema.TextLine(
        title=_(u"Medicine Divination"),
        required=False,
    )

    luck = schema.TextLine(
        title=_(u"Luck Divination"),
        required=False,
    )

    organization = RichText(
        title=_(u"Believer Organization"),
        required=False,
        default_mime_type='text/html',
        output_mime_type='text/html',
        allowed_mime_types=('text/html','text/plain',),
    )

    desc_o = RichText(
        title=_(u"Description Other"),
        required=False,
        default_mime_type='text/html',
        output_mime_type='text/html',
        allowed_mime_types=('text/html','text/plain',),
    )


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Temple(dexterity.Container):
    grok.implements(ITemple)

    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# temple_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class View(grok.View):
    grok.context(ITemple)
    grok.require('zope2.View')
    grok.name('view')

    def t_title(self, value, vocab):
        factory = getUtility(IVocabularyFactory, vocab)
        vocabulary = factory(self)
        try:
            existing = vocabulary.getTerm(value)
            return existing.title
        except LookupError:
            return value

