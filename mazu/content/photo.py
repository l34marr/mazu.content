from five import grok
from plone.directives import dexterity, form

from zope import schema
from plone.app.textfield import RichText
from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedBlobImage

from mazu.content import MessageFactory as _


class IPhoto(form.Schema, IImageScaleTraversable):
    """Photo Interface Class to Define Content-Type Schema
    """

    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/photo.xml to define the content type
    # and add directives here as necessary.

    #form.model("models/photo.xml")

    title = schema.TextLine(
        title=_(u"Title"),
        required=False,
    )

    form.primary('image')
    image = NamedBlobImage(
        title=_(u"Photo"),
    )

    category = schema.List(
        title=_(u"Category"),
        required=False,
    )

    attachesTo = schema.List(
        title=_(u"Attached To"),
        required=False,
    )

    cou = schema.TextLine(
        title=_(u"County"),
        required=False,
    )

    tow = schema.TextLine(
        title=_(u"Town"),
        required=False,
    )

    vil = schema.TextLine(
        title=_(u"Village"),
        required=False,
    )

    year = schema.TextLine(
        title=_(u"Photo Year"),
        required=False,
    )

    month = schema.TextLine(
        title=_(u"Photo Month"),
        required=False,
    )

    day = schema.TextLine(
        title=_(u"Photo Day"),
        required=False,
    )

    owner_name = schema.TextLine(
        title=_(u"Owner Name"),
        required=False,
    )

    owner_org = schema.TextLine(
        title=_(u"Owner Organization"),
        required=False,
    )

    owner_title = schema.TextLine(
        title=_(u"Owner Title"),
        required=False,
    )

    reference = RichText(
        title=_(u"Facing"),
        required=False,
    )

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Photo(dexterity.Item):
    grok.implements(IPhoto)

    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# photo_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class View(grok.View):
    grok.context(IPhoto)
    grok.require('zope2.View')
    grok.name('view')

