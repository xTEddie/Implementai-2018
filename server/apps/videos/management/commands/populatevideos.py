from django.core.management.base import BaseCommand, CommandError
from utils.download_videos import download_videos
from apps.videos.models.video import Video


class Command(BaseCommand):
    help = "Populate Videos"

    def handle(self, *args, **options):
        directory = 'videos'
        file_ids = [
            '1xDPCQ4ntLeHOLTSY6710sHOBFNXyOxtw',
            '1kGvPN3G6wnGTOCqcxAcGLBjgR_9GnX19',
            '1l7UxbwRGmAn61GUJ1rMy-ZlCihJs5wsX',
            '18ZVtge0ZbhaHHLCxFlJ2Ee_fiz7zaP-f'
        ] 
        
        print("Populating videos to the DB...")
        video_paths = download_videos(directory, file_ids)

        for video_path in video_paths:
            video = Video(path=video_path)
            video.save()
        print("DONE!")



 