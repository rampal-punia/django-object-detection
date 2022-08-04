from django.contrib import admin
from .models import ImageDetection


@admin.register(ImageDetection)
class ImageDetectionAdmin(admin.ModelAdmin):
    list_display = ["image", "description", "detectionmodel"]
