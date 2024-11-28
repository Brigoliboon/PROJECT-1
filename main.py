from models import Track, Duration, MusicLibrary, Playlist
from models.interface import *
from database import load, write, __database__
from database.write import *
import math
from models.track import initializedTracks
# Banner = '''
# ==========================================
#      PROJECT 1 - Listen to the Music
# =========================================='''

def displayBanner(title:str)-> None:
    side_space = ' '*5
    line = "="*int(len(title)+10)
    banner = f"{line}\n{side_space}{title}\n{line}"
    print(banner)


if __name__ == "__main__":
    while True:
        print(__database__)
        displayBanner("PROJECT 1 - Listen to the Music")
        Menu("MAIN")
        choice = prompt("Select: ", type=int)
        print(choice)
        match choice:
            case 1: # [1] Enter Music Library
                musiclib:MusicLibrary = load.database("MusicLibrary", filter=True)
                print(musiclib)
                Menu("musiclibrary")
                ml_choice = prompt("Select: ", type=int)

                match ml_choice:
                    case 1: # [1] Search Track
                        pass
                    case 2: # [2] Select Track
                        print(musiclib)
                        selected = prompt("Select Music: ", type=int)
                        track = musiclib.getTrackbyIndex(musiclib.currentPage(), index=selected-1)
                        print(track.__str__(mode= 'full'))
                        Menu("track")
                    case 3: # [3] Play
                        musiclib.play()
                        queue = musiclib.getQueue()
                        print(queue)
                            #initializes Queue
                        q_choice = prompt("Select: ", type=int)
                        match q_choice:
                            case 1: # [1] play/pause
                                if queue.isonPause():
                                    queue.pause(state=False)
                                else:
                                    queue.pause()
                            case 2: # [2] next
                                queue.next()
                            case 3: # [3] previous
                                pass
                            case 4: # [4] Turn {state} repeat
                                if queue.isonRepeat():
                                    queue.onRepeat(state=False)
                                else:
                                    queue.onRepeat()
                            case 5: # [5] Turn {state} shuffle
                                if queue.isShuffled():
                                    queue.shuffle()
                                else:
                                    queue.shuffle(state=False)
                            case 6: # [6] Clear Queue
                                musiclib.stop()
                                continue
                    case 4: # [4] Create Track
                        track = createTrack()
                        if musiclib:
                            musiclib.insert(track)
                        else:
                            print("Music Library was not loaded yet.")

                    case 5: # [5] Next Page
                        print(musiclib)
                        musiclib.pagination.next()
                    case 6: # [6] Previous Page
                        print(musiclib)
                        musiclib.pagination.previous()
                    case 7: # [7] Exit
                        MusiclibDB().save(musiclib)
            case 2: # [2] View List of Playlists
                displayBanner("List of Playlists")
                playlistarray:ArrayList = load.database("PlaylistList", filter=True)
                print(playlistarray.__str__(format="paginate"))
                Menu("playlist-external")
                choice = prompt("Select: ", type=int)

            case 3: # [3] Create Playlist
                pass

            case 4:# [4] View Albums
                pass

            case 5:# [5] Exit
                break