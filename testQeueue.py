class Queue:
    def __init__(self, array:list, by:int = 10) -> None:
        self.__array = array
        self.__itemCount = by
        self.__remainder = len(self.__array) % by
        self.__PaginationLimit = self.__setPaginationLimit()
        self.__PaginationCount = 1
        self.__start = 0
        self.__end = 1
    
    def __increaseCount(self):
        self.__PaginationCount += 1

    def decreaseCount(self):
        self.__PaginationCount -= 1 
    
    def __setStartIndex(self, value:int)-> None:
        self.__start = value
    
    def __setPaginationLimit(self)-> None:
        self.__PaginationLimit = int(len(self.__array)//self.__itemCount)
        if self.__remainder:
            self.__PaginationLimit += 1
    
    def __setEndIndex(self, value:int)-> None:
        if self.__PaginationCount == self.__PaginationLimit:
            self.__end += self.__remainder
        else:
            self.__end += value

    def getCurrentPage(self):
        return self.__array[self.__start, self.__end]

    def next(self):
        pass

    def __loadPage(self):
        self.__setEndIndex(self.__itemCount)
        current = self.getCurrentPage()
        self.__setStartIndex(self.__end)
        count = 0
        while count <= self.__itemCount:
            pass
    def __str__(self) -> str:
        pass