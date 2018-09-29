from django.contrib import admin
from apps.videos.models.video import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'path')


admin.site.register(Video, VideoAdmin)
