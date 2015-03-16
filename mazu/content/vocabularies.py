from zope.schema.interfaces import IVocabularyFactory
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from mazu.content import MessageFactory as _


class data_src(object):
    """ Data Source
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='governmental', title=_(u'Governmental')),
            SimpleTerm(value='academic', title=_(u'Academic')),
            SimpleTerm(value='fieldwork', title=_(u'Fieldwork')),
            SimpleTerm(value='other', title=_(u'Other')),
        )
        return SimpleVocabulary(items)
dataSrcFactory = data_src()

class position(object):
    """ Position Type (Coordinate Type)
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='address', title=_(u'GeoCoder')),
            SimpleTerm(value='gps', title=_(u'GPS')),
            SimpleTerm(value='gisref', title=_(u'GIS Reference')),
            SimpleTerm(value='map', title=_(u'Map')),
            SimpleTerm(value='notyet', title=_(u'Not Yet')),
            SimpleTerm(value='other', title=_(u'Other')),
        )
        return SimpleVocabulary(items)
positionFactory = position()

class deity(object):
    """ Deity Name
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='deity_005', title=_(u'MaZu')),
        )
        return SimpleVocabulary(items)
deityFactory = deity()

class religion(object):
    """ Religion Type
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='buddhism', title=_(u'Buddhism')),
            SimpleTerm(value='taoism', title=_(u'Taoism')),
            SimpleTerm(value='confucianism', title=_(u'Confucianism')),
            SimpleTerm(value='liism', title=_(u'Liism')),
            SimpleTerm(value='ikuantao', title=_(u'IKuanTao')),
            SimpleTerm(value='tienti', title=_(u'TienTi')),
            SimpleTerm(value='tenrikyo', title=_(u'TenRiKyo')),
            SimpleTerm(value='syuanyuanjiao', title=_(u'SyuanYuanJiao')),
            SimpleTerm(value='other', title=_(u'Other')),
        )
        return SimpleVocabulary(items)
religionFactory = religion()

class building(object):
    """ Building Type
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='buddhism', title=_(u'voc_buddhism', default=u'Buddhism')),
            SimpleTerm(value='folk', title=_(u'Folk')),
            SimpleTerm(value='ikuantao', title=_(u'IKuanTao')),
            SimpleTerm(value='private', title=_(u'Private')),
            SimpleTerm(value='vegetarianhall', title=_(u'VegetarianHall')),
            SimpleTerm(value='phoenixhall', title=_(u'PhoenixHall')),
            SimpleTerm(value='taoism', title=_(u'voc_taoism', default=u'Taoism')),
            SimpleTerm(value='other', title=_(u'Other')),
        )
        return SimpleVocabulary(items)
buildingFactory = building()

class funding(object):
    """ Funding Type
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='raising', title=_(u'Raising')),
            SimpleTerm(value='private', title=_(u'Private')),
            SimpleTerm(value='public', title=_(u'Public')),
            SimpleTerm(value='other', title=_(u'Other')),
        )
        return SimpleVocabulary(items)
fundingFactory = funding()

class organizing(object):
    """ Organizing Type
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='person', title=_(u'Person')),
            SimpleTerm(value='committee', title=_(u'Committee')),
            SimpleTerm(value='foundation', title=_(u'Foundation')),
            SimpleTerm(value='deacon', title=_(u'Deacon')),
            SimpleTerm(value='government', title=_(u'Government')),
            SimpleTerm(value='other', title=_(u'Other')),
        )
        return SimpleVocabulary(items)
organizingFactory = organizing()

class accrcy_y(object):
    """ Year Accuracy
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='exact', title=_(u'Exact')),
            SimpleTerm(value='fuzzy', title=_(u'Fuzzy')),
            SimpleTerm(value='unknown', title=_(u'Unknown')),
        )
        return SimpleVocabulary(items)
accrcyYFactory = accrcy_y()

class attachesTo(object):
    """ attachesTo
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='history', title=_(u'Establishment History')),
            SimpleTerm(value='worship', title=_(u'Worship')),
            SimpleTerm(value='introduction', title=_(u'Introduction')),
            SimpleTerm(value='overview', title=_(u'Building Overview')),
            SimpleTerm(value='antiquity', title=_(u'Antiquities')),
            SimpleTerm(value='narrate', title=_(u'Narrate')),
            SimpleTerm(value='non_narrate', title=_(u'Non Narrate')),
            SimpleTerm(value='spatial', title=_(u'Spatial Attribute')),
        )
        return SimpleVocabulary(items)
attachesToFactory = attachesTo()

class publication(object):
    """publication
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='book', title=_(u'Book')),
            SimpleTerm(value='temple', title=_(u'voc_temple', default=u'Temple')),
            SimpleTerm(value='thesis', title=_(u'Thesis')),
            SimpleTerm(value='media', title=_(u'Media')),
            SimpleTerm(value='ancient', title=_(u'Ancient')),
            SimpleTerm(value='proceeding', title=_(u'Proceeding')),
            SimpleTerm(value='periodical', title=_(u'Periodical')),
            SimpleTerm(value='paper', title=_(u'Paper')),
            SimpleTerm(value='journal', title=_(u'Journal')),
            SimpleTerm(value='other', title=_(u'Other')),
        )
        return SimpleVocabulary(items)
publicationFactory = publication()

class database(object):
    """database
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='publication', title=_(u'Publication DB')),
            SimpleTerm(value='archive', title=_(u'Archive DB')),
            SimpleTerm(value='mainland', title=_(u'Mainland DB')),
            SimpleTerm(value='mazu', title=_(u'MaZu DB')),
            SimpleTerm(value='religion', title=_(u'Religion DB')),
            SimpleTerm(value='folk', title=_(u'Folk DB')),
            SimpleTerm(value='foreign', title=_(u'Foreign DB')),
        )
        return SimpleVocabulary(items)
databaseFactory = database()

class study(object):
    """study
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='general', title=_(u'General')),
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
            SimpleTerm(value='document', title=_(u'Document')),
            SimpleTerm(value='arts', title=_(u'Arts')),
            SimpleTerm(value='economics', title=_(u'Economics')),
            SimpleTerm(value='other', title=_(u'Other')),
        )
        return SimpleVocabulary(items)
studyFactory = study()

