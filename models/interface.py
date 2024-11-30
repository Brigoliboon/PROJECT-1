import sys
from models import MusicLibrary, Playlist, ArrayList, Track, Duration, Queue

from database.database import Database, MusiclibDB, PLList, AlbumList

options = {"Main": [
    "Enter Music Library",
    "View List of Playlists",
    "Create Playlist",
    "View Albums",
    "Exit"
],
"track": [
    "Add to a Playlist",
    "Delete",
    "Exit"
],
"musiclibrary": [
    "Search",
    "Select",
    "Play",
    "Create Track",
    "Next Page",
    "Previous Page",
    "Exit"
],
"playlist-internal": [
    "Play",
    "Next Page",
    "Previous Page",
    "Exit"
],
"playlist-external": [
    "Select Playlist",
    "Next Page",
    "Previous Page",
    "Exit"
],
'queue':[]
}

def Menu(interface:str, queueStatus=[None, None, None]):
    queueInterface = [
    "{}".format("Play" if queueStatus[0] else 'Pause'),
    "Next",
    "Previous",
    "Turn {} repeat".format("Off" if queueStatus[1] else 'On'),
    "Turn {} shuffle".format("Off" if queueStatus[2] else 'On')
]
    if interface in options:
        count = 0
        if interface == 'queue':
            current = queueInterface
        else:
            current = options[interface]
        for choice in current:
            count +=1
            print(f"[{count}] {choice}")

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
    
def __inputDuration():
    print("Enter Duration")
    hh = prompt("Hour: ")
    mm = prompt("Minute: ")
    ss = prompt("Second: ")
    return Duration(hh, mm, ss)

def createTrack():
    title = prompt("Track title: ")
    artist = __inputArtist()
    album = prompt("Enter Album: ")
    duration = __inputDuration()
    return Track(title, artist, album, duration)

def createPlaylist():
    title = prompt("Playlist title: ")
    return Playlist(title)

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

class Interface:
    prompt_mess = 'Enter choice: '

    def __track(self, t:Track):
        Menu('track')
        choice = prompt(self.prompt_mess, int)
        match choice:
            case 1:
                pass
            case 2:
                pass
            case 3:
                return

    def main(self):
        Banner = '''
==========================================
     PROJECT 1 - Listen to the Music
=========================================='''
        print(Banner)
        musiclib:MusicLibrary = MusiclibDB().load()
        playlists:ArrayList = PLList().load()
        albums:ArrayList = AlbumList().load()
        Menu('Main') # displays the main interface
        choice = prompt(self.prompt_mess, type=int)
        match choice:
            case 1: # [1] Enter Music Library
                self.__musiclib(musiclib)
                
            case 2: # [2] View List of Playlists
                self.__externalPlaylist(playlists)

            case 3: # [3] Create Playlist <- problem(30%)
                pl = createPlaylist()
                
            case 4: # [4] View Albums <- problem(20%)
                pass

            case 5: # [5] Exit
                MusiclibDB().save()
                PLList().save()
                Database.saveDB()
                exit()
    
    # 80%
    def __musiclib(self, musiclib:MusicLibrary):
        while True:
            print(musiclib)
            Menu('musiclibrary')
            choice = prompt(self.prompt_mess, type=int)

            match choice:
                case 1: # [1] Search Track
                    track:Track = musiclib.search() # <- Problem (20%)
                    if track:
                        self.__track(track)
                    else:
                        print("Track not Found.")

                case 2: # [2] Select Track
                    print(musiclib)
                    selected = prompt("Select Music: ", type=int)
                    track = musiclib.getTrackbyIndex(musiclib.currentPage(), index=selected-1)
                    print(track.__str__(mode= 'full'))
                    self.__track(track) # Enters track interface

                case 3: # [3] Play
                    queue = musiclib.getQueue()
                    self.__queue(queue, parent=musiclib)

                case 4:
                    track = createTrack()
                    if musiclib:
                        musiclib.insert(track)
                    else:
                        print("Music Library was not loaded yet.")

                case 5: # [5] Next Page
                    musiclib.pagination.next()

                case 6:
                    musiclib.pagination.previous()

                case 7:
                    break
    
    # 100%
    def __internalPlaylist(self, playlist:Playlist):
        banner = """
================================
            PLAYLISTS
================================
"""
        while True:
            print(banner)
            Menu('playlist-internal')
            choice = prompt(self.prompt_mess, type=int)
            match choice:
                case 1: # Play
                    q = playlist.getQueue()
                    self.__queue(q)
                case 2: # Next Page
                    playlist.pagination.next()

                case 3: # Previous Page
                    playlist.pagination.previous()

                case 4: # Exit
                    break
    
    # 100%
    def __externalPlaylist(self, playlists:ArrayList):
        banner = """
================================
            PLAYLISTS
================================
"""
        while True:
            print(banner)
            print(playlists.__str__(format="paginate"))
            Menu('playlist-external')
            choice = prompt(self.prompt_mess, type=int)
            match choice:
                case 1: # Select Playlist
                    choice = prompt(self.prompt_mess, type=int)
                    try: 
                        playlists.getItemPage(choice)
                    except IndexError as err:
                        print(f"Error message: {err}")
                        continue

                case 2: # Next Page
                    playlists.pagination.next()
                case 3: # Previous Page
                    playlists.pagination.previous()
                case 4: # Exit
                    break
    
    # 100%
    def __queue(self, queue:Queue, parent:MusicLibrary):
        while True:
            print(queue)
            Menu('queue', queueStatus=[queue.isonPause(), queue.isonRepeat(), queue.isShuffled()])
            #initializes Queue
            q_choice = prompt("Enter choice: ", type=int)
            match q_choice:
                case 1: # [1] play/pause
                    if queue.isonPause():
                        queue.pause(state=False)
                    else:
                        queue.pause()
                case 2: # [2] next
                    queue.next()
                case 3: # [3] previous
                    queue.previous()
                case 4: # [4] Turn {state} repeat
                    if queue.isonRepeat():
                        queue.onRepeat(state=False)
                    else:
                        queue.onRepeat()
                case 5: # [5] Turn {state} shuffle
                    if queue.isShuffled():
                        queue.shuffle(state=False)
                    else:
                        queue.shuffle()

                case 6:
                    parent.stop()
                    break
                            