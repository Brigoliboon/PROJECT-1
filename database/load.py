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

def parsetoTrack(file:list[dict]):
    tracks = []
    for track in file:
        print(track)
        temp = Track(track["track_title"], track["artist_name"], track["album"], Duration(sec=track['duration']))
        tracks.append(temp)
    return tracks

def raw(p):
    pass
def database(type:str):
    with open(__DB_path, 'r', newline='') as f:
        for row in csv.reader(f):
            if type == row[0]:
                byte = __getb64(row)
                return loadbytes(byte)
        return "type not found in database"

def __getb64(l:list)-> bytes:
    return l[2]

def loadbytes(b64:bytes):
    decoded = base64.b64decode(b64)
    return pickle.loads(decoded)