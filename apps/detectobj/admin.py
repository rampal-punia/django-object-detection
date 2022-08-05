from django.contrib import admin
from .models import InferrencedImage


@admin.register(InferrencedImage)
class InferrencedImageAdmin(admin.ModelAdmin):
    list_display = ["orig_image", "inf_image_path",
                    "model_conf", "custom_model"]
