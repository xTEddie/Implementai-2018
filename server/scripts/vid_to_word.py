from google.cloud import videointelligence
import os 
import json

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\mingh\OneDrive\Documents\code\implement_ai\Implementai2018-7e133461c5fc.json"
vid_path = r"C:\Users\mingh\OneDrive\Documents\code\implement_ai\server\utils\videos"

video_client = videointelligence.VideoIntelligenceServiceClient()
features = [videointelligence.enums.Feature.LABEL_DETECTION]

final_list = []

def extract_information():
    for vid in os.listdir(vid_path):
        os.chdir(vid_path)
        attributes = []
        with open(vid, 'rb') as movie:
            input_content = movie.read()
            file_name = os.path.splitext(vid)[0]         #file_name

        attributes.append(file_name)

        operation = video_client.annotate_video(
        features=features, input_content=input_content)

        print('\nProcessing video {} for label annotations:'.format(file_name))

        result = operation.result(timeout=1000)
        print('\nFinished processing.')

        segment_labels = result.annotation_results[0].segment_label_annotations

        for i, segment_label in enumerate(segment_labels):
            one_attribute = []
            label = segment_label.entity.description        #label
            print('Video label description: {}'.format(
                segment_label.entity.description))
            
            category = ""
            for category_entity in segment_label.category_entities:
                category = category_entity.description      #catgory
                print('\tLabel category description: {}'.format(
                    category_entity.description))

            confidence = ""
            for i, segment in enumerate(segment_label.segments):
                start_time = (segment.segment.start_time_offset.seconds +
                            segment.segment.start_time_offset.nanos / 1e9)
                end_time = (segment.segment.end_time_offset.seconds +
                            segment.segment.end_time_offset.nanos / 1e9)
                positions = '{}s to {}s'.format(start_time, end_time)
                confidence = segment.confidence             #confidence
                print('\tSegment {}: {}'.format(i, positions))
                print('\tConfidence: {}'.format(confidence))
            
            one_attribute.append(label)
            one_attribute.append(category)
            one_attribute.append(confidence)

            attributes.append(one_attribute)
            print('\n')
        
        final_list.append(attributes)            
    
    print(final_list)
    with open('data.json', 'w') as outfile:
        json.dump(final_list, outfile)
    print('done')    

if __name__ == "__main__":
    extract_information()