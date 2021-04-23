from django.contrib import admin
from django.utils.html import format_html
from .models import Youtuber


class YtAdmin(admin.ModelAdmin):
    def myPhoto(self, object):
        return format_html('<img src={} height="40"/>'.format(object.photo.url))

    list_display = ('id',  'myPhoto', 'name', 'subs_count', 'is_featured')
    search_fields = ('name', 'camera')
    list_filter = ('city', 'camera')
    list_display_links = ('name', 'id', 'myPhoto')
    # list_editable = ('is_featured',)


# Register your models here.
admin.site.register(Youtuber, YtAdmin)
