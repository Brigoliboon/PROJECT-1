import sys
sys.path.append("models\\track\\")
sys.path.append("models\\")
from avltree.trackavltree import *

class MusicLibrary(TrackAVLTree):
    def __init__(self):
        """Initializes the MusicLibrary, setting up the AVL tree and pagination."""
        super().__init__()


    def compare(self, t1:Track, t2:Track, by:str="title"):
        match by:
            case "title":
                result = self._compareValues(t1.getTitle(), t2.getTitle())
                if not result:
                    return self.compare(t1, t2, by="artist")
    
            case "artist":
                result = self._compareValues(t1.getArtist(), t2.getArtist())
                if not result:
                    return self.compare(t1, t2, "album")
        
            case "album":
                result = self._compareValues(t1.getAlbum(), t2.getAlbum())
                if not result:
                    return self.compare(t1, t2, "track")
        
            case "track":
                result = self._compareValues(str(t1.getDuration()), str(t2.getDuration()))
                if not result:
                    t1.incrOccurence() #todo: increment occurences

        return result
    
    @staticmethod
    def getTrackbyIndex(arr:list[Track], index:int)-> Track:
        """
        Retrieves a Track from the list by its index.
        
        Args:
            arr (list[Track]): The list of Track objects.
            index (int): The index of the track to retrieve.
        
        Raises:
            AssertionError: If the index is out of range.
        
        Returns:
            Track: The Track object at the specified index.
        """
        assert index < len(arr) and index >= 0, "Index out of range"
        return arr[index]

    def __str__(self) -> str:
        """
        Returns a string representation of the MusicLibrary, including the tracks and pagination info.
        
        Returns:
            str: A formatted string representing the music library.
        """
        return f"""
==================================
          MUSIC LIBRARY
==================================
Tracks:
{super().loadPage(counter=True)}

{self.pagination}
"""