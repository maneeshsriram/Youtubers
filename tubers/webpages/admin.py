from django.contrib import admin
from .models import Slider, Team, aboutData, HeaderData
from django.utils.html import format_html


class SiderAdmin(admin.ModelAdmin):

    def myPhoto(self, object):
        return format_html('<img src={} height="60" />'.format(object.photo.url))

    list_display = ('myPhoto', 'headline', 'subtitle', 'button_text')


class TeamAdmin(admin.ModelAdmin):

    def myPhoto(self, object):
        return format_html('<img src={} height="40"/>'.format(object.photo.url))

    list_display = ('id', 'myPhoto', 'first_name', 'role', 'created_date')
    list_display_links = ('first_name', 'id')
    search_fields = ('first_name', 'role')
    list_filter = ('role',)


# Register your models here.
admin.site.register(Slider, SiderAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(aboutData)
admin.site.register(HeaderData)
