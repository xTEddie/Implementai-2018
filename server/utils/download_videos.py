import json
import os
import requests

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()
    params = dict(id=id)
    response = session.get(URL, params=params, stream = True)
    token = get_confirm_token(response)

    if token:
        params = dict(
            id=id, 
            confirm=token
        )        
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # Filter out keep-alive new chunks
                f.write(chunk)

def download_videos(directory, file_path=None):
    # Get file_infos from .json file
    if not file_path:
        file_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'video_ids.json')
    file_infos = json.load(open(file_path))

    if not os.path.exists(directory):
        os.mkdir(directory)

    video_paths = list()
    for file_info in file_infos:         
        video_file_name = '{}.mp4'.format(file_info['name'])
        destination = os.path.join(directory, video_file_name)                
        download_file_from_google_drive(file_info['id'], destination)
        print("Downloaded {}".format(destination))
        video_paths.append(destination)        
    return video_paths

if __name__ == "__main__":
    directory = 'videos'
    download_videos(directory)
