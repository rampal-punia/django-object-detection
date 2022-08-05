import os

from django.conf import settings
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

    custommodel = models.ForeignKey("modelmanager.MLModel",
                                    verbose_name="Custom ML Models",
                                    on_delete=models.DO_NOTHING,
                                    null=True,
                                    related_name="detectedimages",
                                    help_text="Model used for detection",
                                    )
    detectioninfo = models.JSONField(null=True, blank=True)

    yolomodel = models.CharField(_('YOLOV5 Models'),
                                 max_length=250,
                                 null=True,
                                 blank=True
                                 )

    @property
    def get_inferrenced_imageurl(self):
        return self.inferrenceimage.url

    def yoloweights_rootdir(self, modelname):
        yolo_weightsdir = settings.YOLOV5_WEIGHTS_ROOT
        self.yolomodel = os.path.join(yolo_weightsdir, modelname)

    def __str__(self):
        return str(self.image)
