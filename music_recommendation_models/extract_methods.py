import pandas as pd
import numpy as np
data=pd.read_csv("mood_music_dataset.csv")
data.shape
data.head()
def song_id(song_name):
    p=np.array(data[data['name'] == song_name]["id"])
    #c=p[0]
    return p
def song_name(song_id):
    p=np.array(data[data['id'] == song_id]["name"])
    c=p[0]
    return c
def song_features(song_id):
    p=np.array(data[data['id'] == song_id][['length','danceability','acousticness','energy','instrumentalness','liveness','valence',
                                'loudness','speechiness','tempo']])
    return p
def artist_name(song_id):
    a=np.array(data[data['id']==song_id]['artist'])
    return a
def album_name(song_id):
    album=np.array(data[data.id==song_id]['album'])
    return album

