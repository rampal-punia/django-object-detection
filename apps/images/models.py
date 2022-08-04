import os

from django.db import models
from django.conf import settings
from django.urls import reverse
from config.models import CreationModificationDateBase


class ImageSet(CreationModificationDateBase):
    name = models.CharField(
        max_length=100, help_text="eg. Delhi-trip, Tajmahal, flowers")
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='imagesets',
                             on_delete=models.CASCADE
                             )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("images:imageset_detail_url", kwargs={"pk": self.pk})


class ImageFile(models.Model):
    image_set = models.ForeignKey('images.ImageSet',
                                  related_name="images",
                                  on_delete=models.CASCADE,
                                  help_text="Image Set of the uploading images"
                                  )
    image = models.ImageField(upload_to="dz_images")

    @property
    def get_imageurl(self):
        return self.image.url

    @property
    def get_imagepath(self):
        return self.image.path

    @property
    def get_filename(self):
        return os.path.split(self.image.path)[-1]

    def get_delete_url(self):
        return reverse("images:images_list_url", kwargs={"pk": self.image_set.id})
