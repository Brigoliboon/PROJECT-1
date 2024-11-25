from models.interface import *
from models import Track,Duration, Playlist, MusicLibrary, ArrayList
from database import load
import math
import sys
import os
print(os.getcwd())
# Banner = '''
# ==========================================
#      PROJECT 1 - Listen to the Music
# =========================================='''

def displayBanner(title:str)-> None:
    side_space = ' '*5
    line = "="*int(len(title)+10)
    banner = f"{line}\n{side_space}{title}\n{line}"
    print(banner)
t1 = Track('Blinding Lights', 'The Weeknd', 'After Hours', Duration(minute=3, sec=20))
t2 = Track('Watermelon Sugar', 'Harry Styles', 'Fine Line', Duration(minute=2, sec=6))
t3 = Track('Levitating', 'Dua Lipa', 'Future Nostalgia', Duration(minute=3, sec=23))
t4 = Track('Shape of You', 'Ed Sheeran', '÷ (Divide)', Duration(minute=4, sec=23))
t5 = Track('Good 4 U', 'Olivia Rodrigo', 'SOUR', Duration(minute=3, sec=14))
t6 = Track('Stay', 'The Kid LAROI & Justin Bieber', 'F*CK LOVE 3: OVER YOU', Duration(minute=2, sec=35))
t7 = Track('Peaches', 'Justin Bieber', 'Justice', Duration(minute=3, sec=17))
t8 = Track('Kiss Me More', 'Doja Cat feat. SZA', 'Planet Her', Duration(minute=3, sec=24))
t9 = Track('Save Your Tears', 'The Weeknd', 'After Hours', Duration(minute=3, sec=35))
t10 = Track('Montero (Call Me By Your Name)', 'Lil Nas X', 'Montero', Duration(minute=2, sec=17))

# ml = MusicLibrary()
# ml.insert(t1)
# ml.insert(t2)
# ml.insert(t3)
# ml.insert(t4)
# ml.insert(t5)
# ml.insert(t6)
# ml.insert(t7)
# ml.insert(t8)
# ml.insert(t9)
# ml.insert(t10)

if __name__ == "__main__":
    while True:
        displayBanner("PROJECT 1 - Listen to the Music")
        Menu("MAIN")
        choice = prompt("Select: ", type=int)
        print(choice)
        match choice:
            case 1: # [1] Enter Music Library
                musiclib:MusicLibrary = load.database("MusicLibrary")
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
                        print(musiclib.getQueue())
                        
                    case 4: # [4] Create Track
                        pass
                    case 5: # [5] Next Page
                        pass
                    case 6: # [6] Previous Page
                        pass
                    case 7: # [7] Exit
                        continue
        
            case 2: # [2] View List of Playlists
                displayBanner("List of Playlists")
                playlistarray:ArrayList = load.database("PlaylistList")
                print(playlistarray.__str__(format="paginate"))
                Menu("playlist-external")
                choice = prompt("Select: ", type=int)

            case 3: # [3] Create Playlist
                pass

            case 4:# [4] View Albums
                pass

            case 5:# [5] Exit
                pass