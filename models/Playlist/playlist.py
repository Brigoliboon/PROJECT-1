import sys
sys.path.append("models\\")
sys.path.append("models\\Queue\\")
from track import Track
from datetime import datetime, timedelta
from avltree import TrackAVLTree
from track import *

class Playlist(TrackAVLTree):
    """
    Represents a music playlist, containing tracks and providing functionality
    to manage and compare them. Inherits from TrackAVLTree for track organization.
    """
    def __init__(self, title:str):
        super().__init__()
        self.__title = title
        self.__dateCreated = datetime.today()

    def getTitle(self):
        """
        Returns a string representation of the MusicLibrary, including the tracks and pagination info.
        
        Returns:
            str: A formatted string representing the music library.
        """
        return self.__title
    
    def getDateCreated(self):
        """
        Returns the date and time when the playlist was created.

        Returns:
            datetime: The date and time of playlist creation.
        """
        return self.__dateCreated
    
    def getQueue(self):
        """
        Returns the queue associated with the playlist for managing track playback order.

        Returns:
            Queue: The queue of tracks in the playlist.
        """
        return self.__queue

    def insert(self, value:Track):
        super().insert(value)
        self.__addDuration(value.getDuration())

    def __addDuration(self, duration:timedelta):
        """
        Adds the duration of a track to the total duration of the playlist.

        Args:
            duration (Duration): The duration to be added to the total duration.

        Raises:
            AssertionError: If the provided duration is not a Duration object.
        """
        assert type(duration) is timedelta, "Invalid argument. duration must be a Duration object."
        self.getDuration().__add__(duration)

    def merge_sort(self, by="datetime"):
        arr = self.inorder(self.root).getArrayList()
        if len(arr) > 1:
            mid = len(arr) // 2  # Find the middle of the array
            left_half = arr[:mid]  # Divide the array elements into 2 halves
            right_half = arr[mid:]

            self.merge_sort(left_half, by)  # Sort the first half
            self.merge_sort(right_half, by)  # Sort the second half

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(left_half) and j < len(right_half):
                if self.compare(left_half[i], right_half[j], by) < 0:  # Use compare method
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    def compare(self, t1:Track, t2:Track, by:str="datetime"):
        temp = ""
        match by:
            case "datetime":
                result = self._compareValues(t1.getDateTime(), t2.getDateTime())
                if not result:
                    temp = "title"

            case "title":
                result = self._compareValues(t1.getTitle(), t2.getTitle())
                if not result:
                    temp = "artist"
    
            case "artist":
                result = self._compareValues(t1.getArtist(), t2.getArtist())
                if not result:
                    temp = 'album'
        
            case "album":
                result = self._compareValues(t1.getAlbum(), t2.getAlbum())
                if not result:
                    temp = 'duration'

            case "duration":
                result = self._compareValues(str(t1.getDuration()), str(t2.getDuration()))
                if not result:
                    t1.incrOccurence()

        if temp != "":
            return self.compare(t1,t2, temp)
        return result
    
    @classmethod
    def createplaylist(cls, title:str):
        return cls(title)

    def __str__(self) -> str:
        """
        Returns a string representation of the MusicLibrary, including the tracks and pagination info.
        
        Returns:
            str: A formatted string representing the music library.
        """
        return f"""
==================================
            Playlist
==================================
Playlist Name: {self.__title}
Total Duration: {Track.formatduration(self.getDuration(), 'display')}
Tracks:
{self.loadPage(counter=False)}

{self.pagination}
"""
