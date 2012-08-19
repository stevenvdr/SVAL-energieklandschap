from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from models import GalleryPlugin, ImagePlugin
    
class CMSGalleryPlugin(CMSPluginBase):
    model = GalleryPlugin
    name = _("Photo Slider")
    render_template = "photologue_plugin_gallery.html"

    def render(self, context, instance, placeholder):
        context.update({
            'instance':instance,
            'photos':instance.gallery.public(),
        })
        return context

class CMSImagePlugin(CMSPluginBase):
    model = ImagePlugin
    name = _("Image")
    render_template = "photologue_plugin_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({
            'instance':instance,
            'image':instance.image,
        })
        return context

plugin_pool.register_plugin(CMSGalleryPlugin)
plugin_pool.register_plugin(CMSImagePlugin)
