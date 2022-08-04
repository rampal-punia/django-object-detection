from django.contrib import admin

from .models import MLModel


@admin.register(MLModel)
class MlModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'uploader', 'version', 'public']
    list_display_links = ['id', 'name']
