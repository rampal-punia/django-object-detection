import os
import yaml

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.urls import reverse

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
    class_filename = models.CharField(_('Class FileName'),
                                      max_length=100,
                                      null=True,
                                      help_text='Name for the class file'
                                      )
    class_file = models.FileField(_('Ml Model Classes file'),
                                  upload_to=model_classfile_upload_path,
                                  validators=[FileExtensionValidator(
                                      allowed_extensions=[
                                          'txt', 'TXT', 'names', 'names', 'yaml', 'YAML']
                                  )],
                                  help_text='Ml Model classes file. Allowed extensions are: .txt, .names, .yaml'
                                  )
    description = models.TextField(_("Model's description"))
    version = models.CharField(_('Ml Model Version'),
                               max_length=51,
                               null=True,
                               blank=True,
                               )

    public = models.BooleanField(default=False)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=('name', 'uploader'),
            name='unique_model_by_user'
        )]

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

    @property
    def cls_filetype(self):
        return os.path.splitext(self.class_file.name)[-1]

    def get_classesname(self):
        # For YOLO the class names can be extracted from the model instance.
        # classname = model.names
        # This method is for custom model update (for specified classes)
        if self.cls_filetype.lower() == '.yaml':
            with open(self.cls_filepath, 'r') as yaml_cls_file:
                classes = yaml.safe_load(yaml_cls_file)
                return classes.get('names')
        elif self.cls_filetype.lower() == '.txt':
            with open(self.cls_filepath, 'r') as txt_cls_file:
                return txt_cls_file.readlines()

    def get_absolute_url(self):
        return reverse("modelmanager:user_mlmodel_list_url")
