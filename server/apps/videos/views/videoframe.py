from django.urls import path
from rest_framework.generics import ListAPIView
from apps.videos.models.videoframe import VideoFrame
from apps.videos.serializers.videoframe import VideoFrameSerializer


class VideoFrameList(ListAPIView):
    queryset = VideoFrame.objects.all()
    serializer_class = VideoFrameSerializer
