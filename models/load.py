import json
import playlist
import time
from track import Track

path = 'D:\\Central Mindanao University\\2nd Year\\Data Structure and Algorithms\\Projects\\New folder\\database\\finaldb.json'

def loadDefault():
    pl = playlist.PlayList()
    with open(path, 'r') as f:
        musics = []
        data = json.loads(f.read())
    for music in data:
        m = Track(music['title'], music['singer'], music['year'], music['description'], Track.Tags(music['tags']))
        pl.insert(m)
    print(musics)
    return pl

def checkDuplicate():
    songs = []
    duplicated = []

    with open(path, 'r') as f:
        data:list = json.loads(f.read())

    for music in data:
        song = f'{music["title"]} - {music["singer"]}'
        if song in songs:
            duplicated.append(song)
            data.remove(music)
        else:
            songs.append(song)
    with open(path, 'w') as f:
        f.write(json.dumps(data))
    print(duplicated)

p = loadDefault()
# checkDuplicate()
root = p.getRoot()
print(root)
# p.print_tree(root)