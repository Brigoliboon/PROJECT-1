import sys
sys.path.append('models\\track\\')

from track import Track

class ArrayList:
    def __init__(self, size = 50) -> None:
        self.__size = 0
        self.__arraylist = [None] * size
        self.__capacity = size

    def getSize(self):
        return self.__size
    
    def getArrayList(self) -> list[Track]:
        return self.__arraylist[:self.__size]
    
    def isEmpty(self) -> bool:
        return self.__size == 0
    
    def clear(self):
        self.__arraylist = [None] * self.__capacity

    def insert(self, value:Track):
        if self.__size == self.__capacity:
            self.__increaseCapacity(self.__capacity)
        self.__arraylist[self.__size] = value
        self.__increaseSize()
    
    # not finished yet
    @staticmethod
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
    def _compareValues(p1, p2):
        pass

    def __increaseSize(self):
        self.__size += 1
    
    def __increaseCapacity(self, value:int = 10):
        self.__arraylist += [None]*value
    
    def __str__(self) -> str:
        return str(self.getArrayList())