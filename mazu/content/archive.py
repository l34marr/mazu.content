from five import grok
from plone.directives import dexterity, form

from zope import schema

from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from mazu.content import MessageFactory as _


class IArchive(form.Schema):
    """Archive Interface Class to Define Content-Type Schema
    """

    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/archive.xml to define the content type
    # and add directives here as necessary.
    
    #form.model("models/archive.xml")

    title = schema.TextLine(
        title=_(u"Title"),
    )

    image = NamedBlobImage(
        title=_(u"Image"),
        required=False,
    )

    idno = schema.TextLine(
        title=_(u"ID Number"),
        required=False,
    )

    author = schema.TextLine(
        title=_(u"Author"),
        required=False,
    )

    version = schema.TextLine(
        title=_("Version"),
        required=False,
    )

    material = schema.TextLine(
        title=_("Material"),
        required=False,
    )

    function = schema.TextLine(
        title=_("Function"),
        required=False,
    )

    size = schema.Text(
        title=_("Size"),
        required=False,
    )

    period = schema.TextLine(
        title=_(u"Period"),
        required=False,
    )

    institute = schema.TextLine(
        title=_("Institute"),
        required=False,
    )

    text = RichText(
        title=_(u"Body"),
        required=False,
    )

    attach = NamedBlobImage(
        title=_(u"Attachment"),
        required=False,
    )

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Archive(dexterity.Item):
    grok.implements(IArchive)

    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# jury_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class View(grok.View):
    grok.context(IArchive)
    grok.require('zope2.View')
    grok.name('view')

