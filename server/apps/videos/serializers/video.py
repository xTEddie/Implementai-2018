from rest_framework import serializers
from apps.videos.models.video import Video


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'
