import sys
import json
import base64
import pickle
import csv
from models import *
__DB_path = "database\\database.csv"

def musiclib()-> MusicLibrary:
    pass
def fetchAPI()-> list|dict:
    with open("database\\APIres_sample.json") as f:
        raw = f.read()
        arr = json.loads(raw)
    print(parsetoTrack(arr))

def parsetoTrack(file:list):
    tracks = []
    for track in file:
        print(track)
        temp = Track(track["track_title"], track["artist_name"], track["album"], Duration(sec=track['duration']))
        tracks.append(temp)
    return tracks
print(csv.reader(__DB_path))