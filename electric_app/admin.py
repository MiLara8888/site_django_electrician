from django.contrib import admin
from .models import *

class PriceAdmin(admin.ModelAdmin):
    list_display = ('title','price','cat')
    list_display_links = ('cat','title')
    list_filter = ('cat',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Price,PriceAdmin)
admin.site.register(Category,CategoryAdmin)


