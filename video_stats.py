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
    except requests.exceptions.RequestException as e:
        raise e
if __name__ == "__main__":
    get_player_id()