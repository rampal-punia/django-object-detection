import os
from PIL import Image as I

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from config.models import CreationModificationDateBase


class ImageSet(CreationModificationDateBase):
    name = models.CharField(max_length=100,
                            help_text="eg. Delhi-trip, Tajmahal, flowers"
                            )
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='imagesets',
                             on_delete=models.CASCADE
                             )
    dirpath = models.CharField(max_length=150, null=True, blank=True)
    public = models.BooleanField(default=False)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['user', 'name'],
            name='unique_imageset_by_user')]

    def __str__(self):
        return f'{self.name.capitalize()}'

    def get_dirpath(self):
        rootdir = os.path.join(self.user.username, self.name)
        return rootdir

    def get_absolute_url(self):
        return reverse("images:imageset_detail_url", kwargs={"pk": self.pk})


def imageset_upload_images_path(instance, filename):
    return f'{instance.image_set.dirpath}/images/{filename}'


class ImageFile(models.Model):
    name = models.CharField(_('Image Name'), max_length=150, null=True)
    image_set = models.ForeignKey('images.ImageSet',
                                  related_name="images",
                                  on_delete=models.CASCADE,
                                  help_text="Image Set of the uploading images"
                                  )
    image = models.ImageField(upload_to=imageset_upload_images_path)

    is_inferenced = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @ property
    def get_imageurl(self):
        return self.image.url

    @ property
    def get_imagepath(self):
        return self.image.path

    @ property
    def get_filename(self):
        return os.path.split(self.image.url[-1])

    @ property
    def get_imgshape(self):
        im = I.open(self.get_imagepath)
        return im.size

    def get_delete_url(self):
        return reverse("images:images_list_url", kwargs={"pk": self.image_set.id})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = I.open(self.get_imagepath)
        if img.height > 640 or img.width > 640:
            output_size = (640, 640)
            img.thumbnail(output_size)
            img.save(self.get_imagepath)
