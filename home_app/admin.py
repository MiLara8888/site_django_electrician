from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('header_car', 'header2_car', 'get_html_photo')

    def get_html_photo(self, object):
        if object.image_car:
            return mark_safe(f"<img src='{object.image_car.url}', width=50>")

    get_html_photo.short_description = 'Миниатюра'


class CircleAdmin(admin.ModelAdmin):
    list_display = ('header_circle', 'header2_circle', 'get_html_photo')

    def get_html_photo(self, object):
        if object.image_circle:
            return mark_safe(f"<img src='{object.image_circle.url}', width=50>")


class BigImageAdmin(admin.ModelAdmin):
    list_display = ('header_big', 'header2_big', 'get_html_photo','is_right')

    def get_html_photo(self, object):
        if object.image_big:
            return mark_safe(f"<img src='{object.image_big.url}', width=50>")


admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Circle, CircleAdmin)
admin.site.register(BigImage,BigImageAdmin)
