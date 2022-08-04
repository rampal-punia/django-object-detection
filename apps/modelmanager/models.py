import os

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from config.models import CreationModificationDateBase


User = settings.AUTH_USER_MODEL


def model_upload_path(instance, filename):
    return f'{instance.uploader.username}/ml_models/{instance.name}/{filename}'


def model_classfile_upload_path(instance, filename):
    return f'{instance.uploader.username}/mlclassfiles/{instance.name}/{filename}'


class MLModel(CreationModificationDateBase):
    uploader = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='mlmodels'
                                 )
    name = models.CharField(_('Name'),
                            max_length=100,
                            help_text='Name for the machine learning model'
                            )
    pth_file = models.FileField(_('Upload Model Pt/Pth File'),
                                upload_to=model_upload_path,
                                validators=[FileExtensionValidator(
                                    allowed_extensions=['pt', 'pth']
                                )],
                                help_text='Allowed extensions are: .pt, .pth'
                                )
    class_file = models.FileField(_('Ml Model Classes file'),
                                  upload_to=model_classfile_upload_path,
                                  validators=[FileExtensionValidator(
                                      allowed_extensions=[
                                          'txt', 'TXT', 'names', 'names']
                                  )],
                                  help_text='Ml Model classes file. Allowed extensions are: .txt, .names'
                                  )
    description = models.TextField(_("Model's description"))
    model_version = models.CharField(_('Ml Model Version'),
                                     max_length=51,
                                     null=True,
                                     blank=True,
                                     )

    def __str__(self):
        return f"{self.name}-{self.uploader}"

    @property
    def pth_filepath(self):
        return self.pth_file.path

    @property
    def pth_dirpath(self):
        return os.path.split(self.pth_file.path)[0]

    @property
    def pth_filename(self):
        return os.path.splitext(self.pth_file.name)[0]

    @property
    def cls_filepath(self):
        return self.class_file.path

    @property
    def cls_dirpath(self):
        return os.path.split(self.class_file.path)[0]

    @property
    def cls_filename(self):
        return os.path.splitext(self.class_file.name)[0]

    def get_classname(self):
        with open(self.cls_filepath, 'r') as cls_file:
            classes = cls_file.readlines()
            print(classes)
