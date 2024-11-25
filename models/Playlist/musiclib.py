import sys
sys.path.append("models\\track\\")
sys.path.append("models\\")
from avltree.trackavltree import *

class MusicLibrary(TrackAVLTree):
    def __init__(self):
        super().__init__()
        self.pagination = Pagination(self.getSize())
    
    def compare(self, t1:Track, t2:Track, by:str="title"):
        match by:
            case "title":
                result = self._compareValues(t1.getTitle(), t2.getTitle())
                if not result:
                    return self.compare(t1, t2, by="artist")
    
            case "artist":
                result = self.compare(t1.getArtist(), t2.getArtist())
                if not result:
                    return self.compare(t1, t2, "album")
        
            case "album":
                result = self._compareValues(t1.getAlbum(), t2.getAlbum())
                if not result:
                    return self.compare(t1, t2, "track")
        
            case "track":
                result = self._compareValues(str(t1.getDuration()), str(t2.getDuration()))
                if not result:
                    return "Duplicated track"
        return result
    
    @staticmethod
    def getTrackbyIndex(arr:list[Track], index:int)-> Track:
        assert index < len(arr) and index >= 0, "Index out of range"
        return arr[index]
    
    def currentPage(self)-> list[Track]:
        current =  self.inorder(self.root).getArrayList()
        return current[self.pagination.getStartIndex(): self.pagination.getEndIndex()]

    def __str__(self) -> str:

        return f"""
==================================
          MUSIC LIBRARY
==================================
Tracks:
{self.loadPage(counter=True)}

{self.pagination}
"""

# t1 = Track('Blinding Lights', 'The Weeknd', 'After Hours', Duration(minute=3, sec=20))
# t2 = Track('Watermelon Sugar', 'Harry Styles', 'Fine Line', Duration(minute=2, sec=6))
# t3 = Track('Levitating', 'Dua Lipa', 'Future Nostalgia', Duration(minute=3, sec=23))
# t4 = Track('Shape of You', 'Ed Sheeran', '÷ (Divide)', Duration(minute=4, sec=23))
# t5 = Track('Good 4 U', 'Olivia Rodrigo', 'SOUR', Duration(minute=3, sec=14))
# t6 = Track('Stay', 'The Kid LAROI & Justin Bieber', 'F*CK LOVE 3: OVER YOU', Duration(minute=2, sec=35))
# t7 = Track('Peaches', 'Justin Bieber', 'Justice', Duration(minute=3, sec=17))
# t8 = Track('Kiss Me More', 'Doja Cat feat. SZA', 'Planet Her', Duration(minute=3, sec=24))
# t9 = Track('Save Your Tears', 'The Weeknd', 'After Hours', Duration(minute=3, sec=35))
# t10 = Track('Montero (Call Me By Your Name)', 'Lil Nas X', 'Montero', Duration(minute=2, sec=17))
# m = MusicLibrary()
# m.insert(t1)
# m.insert(t2)
# print(m.inorder(m.getRoot()))