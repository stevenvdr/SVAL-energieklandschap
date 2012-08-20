from django.utils.translation import ugettext as _

from django.db import models

from cms.models import CMSPlugin
from photologue.models import Gallery, Photo, PhotoSize

class GalleryPlugin(CMSPlugin):
    gallery = models.ForeignKey(Gallery)

    def __unicode__(self):
        return _("Photoslider ") + self.gallery.__unicode__()


class ImagePlugin(CMSPlugin):
    image = models.ForeignKey(Photo)
    width = models.IntegerField(default=0)
    url = models.URLField(max_length=200, blank=True)

    def __unicode__(self):
        return _("Image ") + self.image.__unicode__()
