import os
from django.db import models

def get_image_path(instance, filename):
    return os.path.join('videos', filename)

class Video(models.Model):
    path = models.FileField(upload_to=get_image_path, blank=False, null=False)
