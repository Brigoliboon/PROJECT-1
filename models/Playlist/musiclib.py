from models.track.track import Track, Duration
from models.avltree.avltree import Node
from models.avltree.trackavltree import TrackAVLTree
from models.Queue.Queue import Pagination

class MusicLibrary(TrackAVLTree):
    def __init__(self):
        super().__init__()
        self.pagination = Pagination(self.getSize())
    
    @staticmethod
    def compare(t1:Track, t2:Track, by:str="title"):
        match by:
            case "title":
                result = MusicLibrary._compareValues(t1.getTitle(), t2.getTitle())
                if not result:
                    return MusicLibrary.compare(t1, t2, by="artist")
    
            case "artist":
                result = MusicLibrary.compare(t1.getArtist(), t2.getArtist())
                if not result:
                    return MusicLibrary.compare(t1, t2, "album")
        
            case "album":
                result = MusicLibrary._compareValues(t1.getAlbum(), t2.getAlbum())
                if not result:
                    return MusicLibrary.compare(t1, t2, "track")
        
            case "track":
                result = MusicLibrary._compareValues(str(t1.getDuration()), str(t2.getDuration()))
                if not result:
                    return "Duplicated track"

        return result
    def currentPage(self)-> list[Track]:
        current =  self.inorder(self.root).getArrayList()
        return current[self.pagination.getStartIndex(): self.pagination.getEndIndex()]

    def __str__(self) -> str:
        return f"""
==================================
          MUSIC LIBRARY
==================================
Tracks:
{self.loadPage()}

{self.pagination}
"""

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
m = MusicLibrary()