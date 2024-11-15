from arraylist import ArrayList

class Queue(ArrayList):
    def __init__(self, array:list, size=10) -> None:
        super().__init__(size)
        self.__count = 0
        self.__pagination = 0
        self.__array = array
        self.__start = 0
        self.__end = 1
    
    def getCount(self)-> int:
        return self.__count
    
    def getPagination(self)-> int:
        return self.__pagination
    
    def setPagination(self, pagination:int)-> None:
        self.__pagination = pagination
    
    def getIndex(self)-> int:
        return self.__start

    def setCount(self, count:int) -> None:
        self.__count = count
    
    def setStart(self, start:int)-> None:
        self.__start = start
    
    def increaseEnd(self):
        self.__start

    def nextPage(self)-> None:
        if self.__count < self.__pagination:
            self.incrCount()

        self.setStart(self.__end)

    def loadPage(self)-> None:
        self.__array[self.__start: self.__end]
    
    def incrCount(self) -> None:
        self.__count += 1