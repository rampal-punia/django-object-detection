import os

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from config.models import CreationModificationDateBase


class InferrencedImage(CreationModificationDateBase):
    orig_image = models.ForeignKey(
        "images.ImageFile",
        on_delete=models.CASCADE,
        related_name="detectedimages",
        help_text="Main Image",
        null=True,
        blank=True
    )

    inf_image_path = models.CharField(max_length=250,
                                      null=True,
                                      blank=True
                                      )

    custom_model = models.ForeignKey("modelmanager.MLModel",
                                     verbose_name="Custom ML Models",
                                     on_delete=models.DO_NOTHING,
                                     null=True,
                                     blank=True,
                                     related_name="detectedimages",
                                     help_text="Machine Learning model for detection",
                                     )
    detection_info = models.JSONField(null=True, blank=True)

    YOLOMODEL_CHOICES = [
        ('yolov5s.pt', 'yolov5s.pt'),
        ('yolov5m.pt', 'yolov5m.pt'),
        ('yolov5l.pt', 'yolov5l.pt'),
        ('yolov5x.pt', 'yolov5x.pt'),
    ]

    yolo_model = models.CharField(_('YOLOV5 Models'),
                                  max_length=250,
                                  null=True,
                                  blank=True,
                                  choices=YOLOMODEL_CHOICES,
                                  help_text="Selected yolo model will download. \
                                 Requires an active internet connection."
                                  )

    model_conf = models.DecimalField(_('Model confidence'),
                                     decimal_places=2,
                                     max_digits=4,
                                     null=True,
                                     blank=True)

    @property
    def get_inferrenced_imageurl(self):
        return self.inferrenceimage.url

    def yoloweights_rootdir(self, modelname):
        yolo_weightsdir = settings.YOLOV5_WEIGHTS_ROOT
        self.yolomodel = os.path.join(yolo_weightsdir, modelname)
