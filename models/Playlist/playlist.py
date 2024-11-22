from avltree import AVLTree
from datetime import datetime
from track import Track, Duration
from Queue import Queue
from arraylist import ArrayList
import json

__database_path = 'D:\\Central Mindanao University\\2nd Year\\Data Structure and Algorithms\\Projects\\Project 1\\database\\musicdb.json'

class Playlist(AVLTree):
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
    
    def __createQueue(self):
        array = self.inorder().getArrayList()
        self.__queue = Queue(array)

def loadDB(path:str = __database_path):
    pl = Playlist("Music Library")

    with open(path, 'r') as f:
        data = json.loads(f.read())

    for music in data:
        m = Track(music['title'], music['singer'], music['year'], music['description'], Track.Tags(music['tags']))
        pl.insert(m)

    return pl