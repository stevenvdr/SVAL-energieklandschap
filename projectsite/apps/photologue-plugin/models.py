from django.db import models

from cms.models import CMSPlugin
from photologue.models import Gallery, Photo, PhotoSize

class GalleryPlugin(CMSPlugin):
    gallery = models.ForeignKey(Gallery)

    def __unicode__(self):
        return "Fotoslider " + self.gallery.__unicode__()


class ImagePlugin(CMSPlugin):
    image = models.ForeignKey(Photo)
    width = models.IntegerField(default=0)
    url = models.URLField(max_length=200, blank=True)

    def __unicode__(self):
        return "Afbeelding " + self.image.__unicode__()
