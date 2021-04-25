from django.contrib import admin
from django.utils.html import format_html
from .models import Hiretuber

# Register your models here.


class hiretuberAdmin(admin.ModelAdmin):

    def mes(self, object):
        if len(object.message) > 20:
            message = object.message[:20] + "..."
            return format_html(message)
        else:
            return format_html(object.message)

    list_display = ('user_id', 'first_name', 'email',
                    'tuber_id', 'tuber_name', 'mes')
    list_display_links = ('first_name',)


admin.site.register(Hiretuber, hiretuberAdmin)
