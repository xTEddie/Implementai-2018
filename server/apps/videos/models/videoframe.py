from django.db import models


class VideoFrame(models.Model):
    video = models.ForeignKey('videos.video', related_name='videoframes', on_delete=models.CASCADE, blank=True)
    current_time = models.CharField(max_length=255)
    violence_status = models.BooleanField(default=True)

    def __str__(self):
        return self.video.path.url