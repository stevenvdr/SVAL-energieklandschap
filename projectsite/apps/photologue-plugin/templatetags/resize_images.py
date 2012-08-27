__author__ = 'steven'

from django import template
from photologue.models import Photo, PhotoSize

from settings import DEFAULT_WIDTH

register = template.Library()

@register.filter
def resize(image, width):
    """Resizes the given image instance tot the given width"""

    if width != 0:
        size, created = PhotoSize.objects.get_or_create(width=width,
            height=0,
            defaults={'name': "_resize_width_%d" % (width)})

        if created:
            image = Photo.objects.get(pk = image.pk)
    else:
        size = PhotoSize.objects.get(name ='default_size')

    return image._get_SIZE_url(size.name)