import requests
import json

import os
from dotenv import load_dotenv
load_dotenv(dotenv_path = "./.env")

API_KEY=os.getenv("API_KEY")
#API_KEY="AIzaSyBNW25D4OYWbBEVXj1CNIKqxdka2HaqKVA"
CHANNEL="MrBeast"

def get_player_id():

    try: 

        url= f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL}&key={API_KEY}"

        response=requests.get(url)
        response.raise_for_status()

        data = response.json()
        #print(json.dumps(data,indent=4))
        #data.["items"][0]["contentDetails"]["relatedPlaylists"].uploads
        channel_playlisId = data["items"][0]["contentDetails"]["relatedPlaylists"]['uploads']
        print(channel_playlisId)

        return channel_playlisId
    except requests.exceptions.RequestException as e:
        raise e

def get_video_ids(playlist_Id):
    video_ids = []  
    pageToken = None
    maxResults=50  
    Base_url = f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={maxResults}&playlistId={playlist_Id}&key={API_KEY}"

    try :
        while True:
            url=Base_url
            if pageToken:
                url+=f"&pageToken={pageToken}"
            response=requests.get(url)
            response.raise_for_status()
            data = response.json() 
            for item in data.get('items',[]):
                video_id =item['contentDetails']['videoId']
                video_ids.append(video_id)
            pageToken = data.get('nextPageToken')
            if not pageToken:
                break
        return video_ids

    except requests.exceptions.RequestException as e:
        raise e

if __name__ == "__main__":
    playlistId = get_player_id()
    print(get_video_ids(playlistId))