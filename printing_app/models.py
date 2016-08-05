import os
import uuid

from django.db import models
from simple_login.models import BaseUser


def get_image_file_path(instance, filename):
    ext = filename.split('.')[-1]
    name = str(uuid.uuid4()).replace('-', '_')
    filename = '{}.{}'.format(name, ext)
    return os.path.join('images', filename)


class User(BaseUser):
    full_name = models.CharField(max_length=255, blank=False)
    address = models.CharField(max_length=2000, blank=False)
    mobile_number = models.CharField(max_length=255, blank=False)


class Album(models.Model):
    owner = models.ForeignKey(
        User,
        blank=False,
        on_delete=models.CASCADE,
        related_name='Owner'
    )
    name = models.CharField(max_length=255, blank=False)

    @property
    def photos(self):
        return Photo.objects.filter(album=self)


class Photo(models.Model):
    album = models.ForeignKey(
        Album,
        blank=False,
        on_delete=models.CASCADE,
        related_name='Photo'
    )
    photo = models.ImageField(blank=False, upload_to=get_image_file_path)
