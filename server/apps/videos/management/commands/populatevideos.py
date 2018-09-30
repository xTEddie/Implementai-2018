import os
from django.core.management.base import BaseCommand, CommandError
from utils.download_videos import download_videos
from apps.videos.models.video import Video
from django.conf import settings


class Command(BaseCommand):
    help = "Populate Videos"

    def handle(self, *args, **options):
        directory = 'videos'
        print("Populating videos to the DB...")
        file_path = os.path.join(settings.BASE_DIR, 'video_ids.json')
        video_paths = download_videos(directory, file_path=file_path)

        for video_path in video_paths:
            # Save video in DB
            video = Video(path=video_path)
            video.save()
        print("DONE!")



 