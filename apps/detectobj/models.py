from django.db import models
from django.utils.translation import gettext_lazy as _
from config.models import CreationModificationDateBase


class ImageDetection(CreationModificationDateBase):
    image = models.ForeignKey(
        "images.ImageFile",
        on_delete=models.CASCADE,
        related_name="detectedimages",
        help_text="Main Image",
        null=True,
        blank=True
    )

    description = models.TextField()

    inferrenceimage = models.ImageField(
        upload_to="inferrenceimages", null=True, blank=True)

    detectionmodel = models.ForeignKey(
        "modelmanager.MLModel",
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="detectedimages",
        help_text="Model used for detection",
    )
    detectioninfo = models.JSONField(null=True, blank=True)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return str(self.image)
