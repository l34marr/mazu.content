from five import grok
from plone.directives import dexterity, form

from zope import schema

from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage

from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

from mazu.content import MessageFactory as _

# Interface class; used to define content-type schema.

class IPublication(form.Schema):
    """
    MaZu Publication Type
    """
    
    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/jury.xml to define the content type
    # and add directives here as necessary.
    
    #form.model("models/publication.xml")

    title = schema.TextLine(
        title=_(u"Title"),
    )

    category = schema.Choice(
        title=_(u"Category"),
        vocabulary='category',
        required=False,
    )

    author = schema.TextLine(
        title=_(u"Author"),
        required=False,
    )

    distribution = schema.TextLine(
        title=_(u"Distribution"),
        required=False,
    )

    date = schema.Date(
        title=_("Date"),
        required=False,
    )

    publisher = schema.TextLine(
        title=_("Publisher"),
        required=False,
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )

    text = RichText(
        title=_(u"Body"),
        required=False,
    )

    url = schema.Text(
        title=_(u"URL"),
        required=False,
    )

    archive = schema.Text(
        title=_(u"Archive"),
        required=False,
    )

    database = schema.List(
        title=_(u"Database"),
        required=False,
        value_type=schema.Choice(
            vocabulary='database',
        ),
    )

    study = schema.List(
        title=_(u"Study"),
        required=False,
        value_type=schema.Choice(
            vocabulary='study',
        ),
    )

    image = NamedBlobImage(
        title=_(u"Image"),
        required=False,
    )

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Publication(dexterity.Item):
    grok.implements(IPublication)
    
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
    grok.context(IPublication)
    grok.require('zope2.View')
    grok.name('view')

    def t_title(self, value, vocab):
        factory = getUtility(IVocabularyFactory, vocab)
        vocabulary = factory(self)
        return vocabulary.getTerm(value).title

