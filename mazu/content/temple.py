from five import grok
from plone.directives import dexterity, form
from plone.indexer import indexer

from zope import schema
from plone.app.textfield import RichText

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

    data_src = schema.TextLine(
        title=_(u"Data Source"),
        required=False,
    )

    position = schema.TextLine(
        title=_(u"Position Type"), #Coordinate Type
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

    religion = schema.TextLine(
        title=_(u"Religion Type"),
        required=False,
    )

    building = schema.TextLine(
        title=_(u"Building Type"),
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

    funding = schema.TextLine(
        title=_(u"Funding Type"),
        required=False,
    )

    funding_o = schema.TextLine(
        title=_(u"Funding Type Other"),
        required=False,
    )

    organizing = schema.TextLine(
        title=_(u"Organizing Type"),
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

    year_accuracy = schema.TextLine(
        title=_(u"Year Accuracy"),
        required=False,
    )

    facing = schema.TextLine(
        title=_(u"Facing"),
        required=False,
    )

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Temple(dexterity.Container):
    grok.implements(ITemple)

    # Add your class methods and properties here

@indexer(ITemple)
def lcityIndexer(obj):
    if len(obj.address) >= 3 and obj.address[2] in (u'\u5e02', u'\u7e23'):
        return obj.address[:3]
    else:
        return None
grok.global_adapter(lcityIndexer, name='lcity')


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

