import os
from django.db import models

def get_video_path(instance, filename):
    return os.path.join('videos', filename)

class Video(models.Model):
    name = models.CharField(max_length=255)
    path = models.FileField(upload_to=get_video_path, blank=False, null=False)

    def __str__(self):
        return self.path.url