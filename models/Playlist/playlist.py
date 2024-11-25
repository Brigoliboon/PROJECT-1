import sys
sys.path.append("models\\")
sys.path.append("models\\Queue\\")
from datetime import datetime
from Queue import Queue
from avltree import TrackAVLTree
from track import *
class Playlist(TrackAVLTree):
    def __init__(self, title:str):
        super().__init__()
        self.__title = title
        self.__dateCreated = datetime.today()
        self.__totalDuration = Duration(hour=0, minute=0, sec=0)
        self.__queue = None

    def getTitle(self):
        return self.__title
    
    def getDateCreated(self):
        return self.__dateCreated
    
    def getDuration(self):
        return self.__totalDuration
    
    def getQueue(self):
        return self.__queue

    def play(self):
        self.__createQueue()
    
    def __addDuration(self, duration:Duration):
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
                
    def __createQueue(self):
        array = self.inorder()
        self.__queue = Queue(array)
