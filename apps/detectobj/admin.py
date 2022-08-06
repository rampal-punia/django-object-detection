from django.contrib import admin
from .models import InferencedImage


@admin.register(InferencedImage)
class InferencedImageAdmin(admin.ModelAdmin):
    list_display = ["orig_image", "inf_image_path",
                    "model_conf", "custom_model"]
