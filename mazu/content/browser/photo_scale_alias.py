from zope.component import getMultiAdapter
from Products.Five.browser import BrowserView


class PhotoScaleAlias(BrowserView):
    """ Scale aliase view for dexterity image content types.

    Allow to use Archetypes scales, for example 'image_preview'.
    Usage: simply register this view with appropriate name like
    'image_preview' or 'image_mini'.
    """

    def _image_scaling(self):
        return getMultiAdapter((self.context, self.request), name='images')

    def get_scale(self):
        return self._image_scaling().scale(*self.__name__.split('_'))

    def __call__(self):
        return self.get_scale().index_html()
