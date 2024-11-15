from track import Track

class Array:
    def __init__(self, size = 50) -> None:
        self.__size = 0
        self.__array = []
        self.__capacity = size

    def getSize(self):
        return self.__size
    
    def getArrayList(self):
        return self.__arraylist[:self.__size]
    
    def clear(self):
        self.__arraylist = [None] * self.__capacity

    def insert(self, value:Track):
        self.__arraylist[self.__size] = value
        self.__increaseSize()

    def remove(self, value:Track):
        pass
    def __increaseSize(self, value:int = 1):
        self.__arraylist += [None]*value
