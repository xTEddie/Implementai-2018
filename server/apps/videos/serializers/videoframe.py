from rest_framework import serializers
from apps.videos.models.videoframe import VideoFrame
from apps.videos.serializers.video import VideoSerializer


class VideoFrameSerializer(serializers.ModelSerializer):
    video = VideoSerializer(read_only=True)

    class Meta:
        model = VideoFrame
        fields = '__all__'
