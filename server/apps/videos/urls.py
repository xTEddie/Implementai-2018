from django.urls import path
from .views.video import VideoList


urlpatterns = [
    path(r'videos', VideoList.as_view())
]

