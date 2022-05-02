from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class PostAdmin(admin.ModelAdmin):
    list_display = ('header', 'time_create','get_html_photo')
    list_display_links = ('header',)
    search_fields = ('header',)
    list_filter = ('time_create',)
    readonly_fields = ('time_create',)

    def get_html_photo(self, object):
        if object.image_preview:
            return mark_safe(f"<img src='{object.image_preview.url}', width=50>")

    get_html_photo.short_description = 'Миниатюра'

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('get_html_photo','product')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}', width=50>")

    get_html_photo.short_description = 'Миниатюра'



admin.site.register(Post, PostAdmin)
admin.site.register(Photo,PhotoAdmin)
