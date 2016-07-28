from django.contrib import admin

from models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'source')
    search_fields = ('title', 'desc')

admin.site.register(Image, ImageAdmin)
