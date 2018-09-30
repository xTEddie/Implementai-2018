from google.cloud import videointelligence
import os 

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\mingh\OneDrive\Documents\code\implement_ai\Implementai2018-7e133461c5fc.json"
vid_path = r"C:\Users\mingh\OneDrive\Documents\code\implement_ai\server\media\videos"

video_client = videointelligence.VideoIntelligenceServiceClient()
features = [videointelligence.enums.Feature.LABEL_DETECTION]

for vid in os.listdir(vid_path):
    os.chdir(vid_path)
    with open(vid, 'rb') as movie:
        input_content = movie.read()

    operation = video_client.annotate_video(
    features=features, input_content=input_content)

    # operation = video_client.annotate_video(
    #     'gs://demomaker/cat.mp4', features=features)
    print('\nProcessing video for label annotations:')

    result = operation.result(timeout=90)
    print('\nFinished processing.')

    # first result is retrieved because a single video was processed
    segment_labels = result.annotation_results[0].segment_label_annotations
    for i, segment_label in enumerate(segment_labels):
        print('Video label description: {}'.format(
            segment_label.entity.description))
        for category_entity in segment_label.category_entities:
            print('\tLabel category description: {}'.format(
                category_entity.description))

        for i, segment in enumerate(segment_label.segments):
            start_time = (segment.segment.start_time_offset.seconds +
                        segment.segment.start_time_offset.nanos / 1e9)
            end_time = (segment.segment.end_time_offset.seconds +
                        segment.segment.end_time_offset.nanos / 1e9)
            positions = '{}s to {}s'.format(start_time, end_time)
            confidence = segment.confidence
            print('\tSegment {}: {}'.format(i, positions))
            print('\tConfidence: {}'.format(confidence))
        print('\n')