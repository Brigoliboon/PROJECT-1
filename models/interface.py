import sys
# from models import MusicLibrary, Playlist, ArrayList, Track, Duration
def Menu(interface:str):
    if interface in options:
        for choice in options:
            print(f"[{choice}] {choice["opt"]}")
def __inputArtist():
    multiple = True
    artists = []
    count = 0
    while multiple:
        count +=1
        artist = prompt("Enter Artist: ")
        if artist == '-':
            break

    if count == 1:
        return artist
    
# def __inputDuration():
#     print("Enter Duration")
#     hh = prompt("Hour: ")
#     mm = prompt("Minute: ")
#     ss = prompt("Second: ")
#     return Duration(hh, mm, ss)

# def createTrack():
#     title = prompt("Track title: ")
#     artist = __inputArtist()
#     album = prompt("Enter Album: ")
#     duration = __inputDuration()
#     return Track(title, artist, album, duration)

def prompt(string:str, type=str|int)->int|str:
    assert type is str or type is int, 'type must only be int or str' 
    initial = input(string)
    if initial == '':
        print(f"User input cannot be empty")
        return prompt(string, type)
    try:
        initial = type(initial)
    except ValueError as err:
        print(f"Error: {err}")
        return prompt(string, type)
    return initial

options = {
    "MAIN": {
        1: {"opt": "Enter Music Library", "func": "MusicLibrary.__str__"},
        2: {"opt": "View List of Playlists", "func": "ArrayList.__str__"},
        3: {"opt": "Create Playlist", "func": "Playlist.createplaylist"},
        4: {"opt": "View Albums", "func":" ArrayList.__str__"},
        5: {"opt": "Exit", "func": "exit"}
    },
    "track": {
        1: {"opt": "Add to a Playlist", "func": None},
        2: {"opt": "Delete", "func": None},
        3: {"opt": "Exit", "func": exit}
    },
    "musiclibrary": {
        1: {"opt": "Search", "func":" MusicLibrary.search"},
        2: {"opt": "Select", "func":" MusicLibrary.getTrackbyInde"},
        3: {"opt": "Play", "func": "MusicLibrary.play"},
        4: {"opt": "Create Track", "func": "createTrack"},
        5: {"opt": "Next Page", "func": "MusicLibrary.pagination.next"},
        6: {"opt": "Previous Page", "func": "MusicLibrary.pagination.previous"},
        7: {"opt": "Exit", "func": None}
    },
    "playlist-internal": {
        1: {"opt": "Play", "func": "Playlist.play"},
        2: {"opt": "Next Page", "func": "Playlist"},
        3: {"opt": "Previous Page", "func": "previousPlaylistPage"},
        4: {"opt": "Exit", "func": "exitInternalPlaylist"}
    },
    "playlist-external": {
        1: {"opt": "Select Playlist", "func": "selectExternalPlaylist"},
        2: {"opt": "Next Page", "func": "nextExternalPlaylistPage"},
        3: {"opt": "Previous Page", "func": "previousExternalPlaylistPage"},
        4: {"opt": "Exit", "func": "exitExternalPlaylist"}
    },
    "queue": {
        1: {"opt": "View Queue", "func": "viewQueue"},
        2: {"opt": "Next", "func": "nextInQueue"},
        3: {"opt": "Previous", "func": "previousInQueue"},
        4: {"opt": "Turn Repeat On", "func": "turnRepeatOn"},
        5: {"opt": "Turn Repeat Off", "func": "turnRepeatOff"}
    }
}