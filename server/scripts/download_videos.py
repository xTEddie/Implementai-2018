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

def download_videos(directory, file_ids):
    if not os.path.exists(directory):
        os.mkdir(directory)

    for file_id in file_ids:         
        video_file_name = '{}.mp4'.format(file_id)
        destination = os.path.join(directory, video_file_name)        
        print("Downloaded {}".format(destination))
        download_file_from_google_drive(file_id, destination)

if __name__ == "__main__":
    directory = 'videos'
    file_ids = [
        '1xDPCQ4ntLeHOLTSY6710sHOBFNXyOxtw',
        '1kGvPN3G6wnGTOCqcxAcGLBjgR_9GnX19',
        '1l7UxbwRGmAn61GUJ1rMy-ZlCihJs5wsX',
        '18ZVtge0ZbhaHHLCxFlJ2Ee_fiz7zaP-f'
    ] 

    download_videos(directory, file_ids)
