import sys

from models.track import Track
sys.path.append("models\\")
sys.path.append("models\\Queue\\")
from datetime import datetime
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
        self.__totalDuration = Duration(hour=0, minute=0, sec=0)

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
    
    def getDuration(self):
        """
        Returns the total duration of all tracks in the playlist.

        Returns:
            Duration: The total duration of the playlist.
        """
        return self.__totalDuration
    
    def getQueue(self):
        """
        Returns the queue associated with the playlist for managing track playback order.

        Returns:
            Queue: The queue of tracks in the playlist.
        """
        return self.__queue

    def insert(self, track: Track):
        self.__addDuration(track.getDuration())
        super().insert(track)
    def __addDuration(self, duration:Duration):
        """
        Adds the duration of a track to the total duration of the playlist.

        Args:
            duration (Duration): The duration to be added to the total duration.

        Raises:
            AssertionError: If the provided duration is not a Duration object.
        """
        assert type(duration) is Duration, "Invalid argument. duration must be a Duration object."
        self.__totalDuration.addDuration(duration)
    
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
Total Duration: {self.getDuration().getMinute()} min {self.getDuration().getSecond()} sec
Tracks:
{self.loadPage(counter=False)}

{self.pagination}
"""
