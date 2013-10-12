from zope.schema.interfaces import IVocabularyFactory
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from mazu.content import MessageFactory as _

class types(object):
    """ types
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='book', title=_(u'Book')),
            SimpleTerm(value='temple', title=_(u'Temple')),
            SimpleTerm(value='thesis', title=_(u'Thesis')),
            SimpleTerm(value='media', title=_(u'Media')),
            SimpleTerm(value='ancient', title=_(u'Ancient')),
            SimpleTerm(value='proceeding', title=_(u'Proceeding')),
            SimpleTerm(value='periodical', title=_(u'Periodical')),
            SimpleTerm(value='paper', title=_(u'Paper')),
            SimpleTerm(value='conference', title=_(u'Conference')),
            SimpleTerm(value='other', title=_(u'Other')),
        )
        return SimpleVocabulary(items)
typesFactory = types()

class databases(object):
    """ databases
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='publication', title=_(u'Publication')),
            SimpleTerm(value='archive', title=_(u'Archive')),
            SimpleTerm(value='mainland', title=_(u'Mainland')),
            SimpleTerm(value='mazu', title=_(u'MaZu')),
            SimpleTerm(value='religion', title=_(u'Religion')),
            SimpleTerm(value='folk', title=_(u'Folk')),
            SimpleTerm(value='foreign', title=_(u'Foreign')),
        )
        return SimpleVocabulary(items)
databasesFactory = databases()

class studies(object):
    """ studies
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='introduction', title=_(u'Introduction')),
            SimpleTerm(value='classic', title=_(u'Classic')),
            SimpleTerm(value='comparison', title=_(u'Comparison')),
            SimpleTerm(value='history', title=_(u'History')),
            SimpleTerm(value='ritual', title=_(u'Ritual')),
            SimpleTerm(value='pilgrimage', title=_(u'Pilgrimage')),
            SimpleTerm(value='organization', title=_(u'Organization')),
            SimpleTerm(value='argument', title=_(u'Argument')),
            SimpleTerm(value='straits', title=_(u'Straits')),
            SimpleTerm(value='politics', title=_(u'Politics')),
            SimpleTerm(value='spread', title=_(u'Spread')),
            SimpleTerm(value='policy', title=_(u'Policy')),
            SimpleTerm(value='community', title=_(u'Community')),
            SimpleTerm(value='region', title=_(u'Region')),
            SimpleTerm(value='temple', title=_(u'Temple')),
            SimpleTerm(value='arts', title=_(u'Arts')),
            SimpleTerm(value='economics', title=_(u'Economics')),
            SimpleTerm(value='other', title=_(u'Other')),
        )
        return SimpleVocabulary(items)
studiesFactory = studies()
