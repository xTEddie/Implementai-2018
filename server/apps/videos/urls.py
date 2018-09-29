from django.urls import path
from .views.video import VideoList
from .views.videoframe import VideoFrameList


urlpatterns = [
    path(r'videos', VideoList.as_view()),
    path(r'videoframes', VideoFrameList.as_view())
]

