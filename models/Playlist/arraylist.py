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
    
    def __increaseSize(self):
        self.__size += 1
    
    def __increaseCapacity(self, value:int = 1):
        self.__arraylist += [None]*value
    
    def __str__(self) -> str:
        return str(self.getArrayList())