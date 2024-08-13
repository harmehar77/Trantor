import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os
import base64
from requests import post, get
import json
import pickle
import numpy as np
import sklearn.tree 
pickle_in = open("dt_genre_classifier","rb") 
genre_classifier = pickle.load(pickle_in)
pickle_in = open("standardscaler","rb") 
scaler = pickle.load(pickle_in)
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


st.title("Song Genre Classifier")
# User inputs
name_track = st.text_input("Enter the song name:")
name_artist = st.text_input("Enter the artist name:")

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
    result = post(url,headers=headers,data=data) #request body
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_track(token, name_track):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={name_track}&type=track&limit=1"

    query_url = url + query
    result = get(query_url,headers=headers)
    json_result = json.loads(result.content)["tracks"]["items"]
    if len(json_result)==0:
        print("No song with given name exists")
        return None 
        
    return json_result[0]

def get_track_features(token,track_id):
    url = "https://api.spotify.com/v1/audio-features/"
    headers = get_auth_header(token)
    query = url + track_id

    result = get(query,headers=headers)
    json_result = json.loads(result.content)
    return json_result

token = get_token()
result = search_for_track(token,name_track)
track_id = result['id']
track_features = get_track_features(token,track_id)

scaled = scaler.transform([track_features])
prediction = genre_classifier.predict(scaled)
genre = {0:'acoustic',1:'classical',2:'club',3:'drum-and-bass',4:'jazz',5:'metal',6:'pop',7:'r-n-b',8:'rock',9:'romance'}

song_genre = genre[prediction[0]]

if st.button("Classify Genre"):
        st.success(f"The genre of '{name_track}' by {name_artist} is: {song_genre}")

else:
    st.error("Song not found. Please check the song and artist names.")