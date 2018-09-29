from django.urls import path
from rest_framework.generics import ListAPIView
from apps.videos.models.video import Video
from apps.videos.serializers.video import VideoSerializer


class VideoList(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
