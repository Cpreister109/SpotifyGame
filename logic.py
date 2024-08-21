from dotenv import load_dotenv
from requests import post, get
import streamlit as st
import base64
import json
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    
    if len(json_result) == 0:
        print("This artist does not exist...")
        return None
    
    return json_result[0]

def get_albums_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums?include_groups=album&limit=50"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["items"]

    return json_result

# FINISH
def get_tracks_in_album(token, album_id):
    url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["items"]
    
    return json_result
# FINISH

def prep_albums(artist):
    token = get_token()
    result = search_for_artist(token, artist)
    artist_id = result["id"]
    albums = get_albums_by_artist(token, artist_id)

    dupe_albums = [
        "folklore: the long pond studio sessions (from the Disney+ special) [deluxe edition]",
        "reputation Stadium Tour Surprise Song Playlist",
        "1989 (Deluxe Edition)",
        "1989",
        "Red (Deluxe Edition)",
        "Red",
        "Speak Now World Tour Live",
        "Speak Now (Deluxe Edition)",
        "Speak Now",
        "Fearless Platinum Edition",
        "Fearless",
        "Live From Clear Channel Stripped 2008"
    ]

    return albums, dupe_albums

def display_albums(artist_albums, duplicate_albums, num_cols, cols):
    for i, album in enumerate(artist_albums):   
        if album['name'] not in duplicate_albums:
            url = album['images'][0]['url']
            print(url)
            name =album['name']
            col = cols[i % num_cols]
            with col:
                with st.container():
                    st.image(url, width=150)
                    st.button(name)

test = get_tracks_in_album(get_token(), "3sJt9QhdFvXiLPtY3oMjFC")
print(test)
