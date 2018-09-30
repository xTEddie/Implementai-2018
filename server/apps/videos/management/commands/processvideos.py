import json
import os
from django.core.management.base import BaseCommand, CommandError
from utils.download_videos import download_videos
from apps.videos.models.video import Video
from apps.videos.models.videoframe import VideoFrame
from django.conf import settings
from django.core.files import File


class Command(BaseCommand):
    help = "Process Videos"

    def handle(self, *args, **options):

        data_file_dir = os.path.dirname(settings.BASE_DIR)
        data_file_path = os.path.join(data_file_dir, 'data', 'labelling', 'Output.txt')

        data = json.load(open(data_file_path))
        for d in data:
            time, name, value = d
            video = Video.objects.get(name=name)
            video_frame = VideoFrame(video=video, current_second=float(time), violence_status=bool(value))
            video_frame.save()

        print("DONE!")



 