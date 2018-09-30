import os
from django.core.management.base import BaseCommand, CommandError
from utils.download_videos import download_videos
from apps.videos.models.video import Video
from django.conf import settings
from django.core.files import File


class Command(BaseCommand):
    help = "Populate Videos"

    def handle(self, *args, **options):
        directory = 'videos'
        print("Populating videos to the DB...")
        file_path = os.path.join(settings.BASE_DIR, 'video_ids.json')
        video_data = download_videos(directory, file_path=file_path)

        for data in video_data:
            # Save video in DB
            local_file = open(data['destination'], 'rb')
            djangofile = File(local_file)
            video = Video(name=data['name'])        
            try:
                video.path.save(data['destination'].replace('videos/', ''), djangofile)
            except:
                pass
            local_file.close()
        print("DONE!")



 