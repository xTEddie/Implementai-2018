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

def download_videos(directory, file_infos):
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
    file_info = [
        # {
        #     "name":"good_0",
        #     "id":'18ZVtge0ZbhaHHLCxFlJ2Ee_fiz7zaP-f'
        # },
        # {
        #     "name":"bad_1",
        #     "id":'1QloRmn9RS-IN-myZTrfXzet97ywu9Udp'
        # },
        # {
        #     "name":"bad_2",
        #     "id":'1xDPCQ4ntLeHOLTSY6710sHOBFNXyOxtw'
        # },
        # {
        #     "name":"bad_3",
        #     "id":'1l7UxbwRGmAn61GUJ1rMy-ZlCihJs5wsX'
        # },
        # {
        #     "name":"bad_0",
        #     "id":'1Mq4bpnmpUKAoh_0ivy6qUtjq_UMk0Qik'
        # },
        # {
        #     "name":"good_1",
        #     "id":'1nLo7Eu-YR6-0u7wWlsEjzT9o2lpKvzYx'
        # },
        # {
        #     "name":"good_2",
        #     "id":'12TDloefN4v88p8bK9WRO3tteS1MC3hkf'
        # },
        # {
        #     "name":"good_3",
        #     "id":'1NYbK5BbstJtMc0i_JsQoCVGTxiU7ZehS'
        # },
        # {
        #     "name":"good_4",
        #     "id":'1KIJywkRGrxqi6wNQ_CniAoAJjPxf0yX4'
        # },
        {
            "name":"good_5",
            "id":'1SNd56icysU5sqj-umRHm9NBuQpsNnP4A'
        },
        # {
        #     "name":"good_6",
        #     "id":'1eZ_fp-3bwGCPzU_9QJmMKC8O5exCqnMy'
        # },
        # {
        #     "name":"good_7",
        #     "id":'1inY87bp0t7eYn955x9I0PIxKiSSdb7BE'
        # },
        # {
        #     "name":"good_8",
        #     "id":'1QmoPvUjG-HlmkM25tlbCDCHGA_PiR2q6'
        # },
        {
            "name":"bad_5",
            "id":'1-ECBUm2aHtEp4fEZ2hje3y1zgtNIOl0E'
        }
    ] 

    download_videos(directory, file_info)
