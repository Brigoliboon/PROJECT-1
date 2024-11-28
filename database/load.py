import json
import base64
import pickle
import csv
from models import *
from . import __DB_path__

def musiclib()-> MusicLibrary:
    pass

def fetchAPI()-> list|dict:
    with open("database\\APIres_sample.json") as f:
        raw = f.read()
        arr = json.loads(raw)
    return parsetoTrack(arr)

def parsetoTrack(file:list[dict]):
    tracks = []
    for track in file:
        print(track)
        temp = Track(track["track_title"], track["artist_name"], track["album"], Duration(sec=track['duration']))
        tracks.append(temp)
    return tracks

def database(type:str='', filter:bool=False):
    with open(__DB_path__, 'r', newline='') as f:
        db = csv.reader(f)
        for row in db:
            if filter:
                if type == row[0]:
                    byte = __getb64(row)
                    return loadbytes(byte)
            else:
                return list(db)
        return "type not found in database"

def __getb64(l:list)-> bytes:
    return l[2]

def loadbytes(b64:bytes):
    decoded = base64.b64decode(b64)
    return pickle.loads(decoded)