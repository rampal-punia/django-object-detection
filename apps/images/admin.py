from django.contrib import admin
from .models import ImageSet, ImageFile


@admin.register(ImageSet)
class ImageSetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'user']
    list_display_links = ['id', 'name']


@admin.register(ImageFile)
class ImageFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_set', 'image', 'is_inferenced']
