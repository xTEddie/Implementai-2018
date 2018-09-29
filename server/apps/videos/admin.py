from django.contrib import admin
from apps.videos.models.video import Video
from apps.videos.models.videoframe import VideoFrame


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'path')

class VideoFrameAdmin(admin.ModelAdmin):
    list_display = ('id', 'video', 'violence_status')

admin.site.register(Video, VideoAdmin)
admin.site.register(VideoFrame, VideoFrameAdmin)
