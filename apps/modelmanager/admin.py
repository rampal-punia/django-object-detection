from django.contrib import admin

from .models import MLModel


@admin.register(MLModel)
class MlModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'uploader', 'model_version', 'public']
    list_display_links = ['id', 'name']
