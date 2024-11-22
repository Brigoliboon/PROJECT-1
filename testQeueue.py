class Queue:
    def __init__(self, array:list, by:int = 10) -> None:
        assert type(by) is int, "invalid item type." 
        self.__array = array
        self.__itemCount = by
        self.__PaginationCount = 1
        self.__setPaginationLimit()

    def getArray(self):
        return self.__array
    
    def getPage(self):
        return self.__PaginationCount
    
    def getStartIndex(self):
        index = (self.__PaginationCount - 1) * self.__itemCount
        return index

    def getEndIndex(self):
        index = self.__PaginationCount * self.__itemCount
        if self.__PaginationCount == self.__PaginationLimit:
            index -= self.__remainder
        return index

    def __increaseCount(self):
        self.__PaginationCount += 1

    def __decreaseCount(self):
        self.__PaginationCount -= 1
    
    def __setPaginationLimit(self)-> None:
        self.__remainder = len(self.__array) % self.__itemCount if len(self.__array)/self.__itemCount >= 1 else 0
        self.__PaginationLimit = int(len(self.__array)//self.__itemCount)
        if self.__remainder:
            self.__PaginationLimit += 1

    def getCurrentPage(self)-> list:
        return self.__array[self.getStartIndex(): self.getEndIndex()]
    
    def previous(self)-> None:
        if self.__PaginationCount > 1:
            self.__decreaseCount()

    def next(self)-> None:
        if self.__PaginationCount < self.__PaginationLimit:
            self.__increaseCount()
    
    def __loadQueue(self):
        items = self.getCurrentPage()
        s = ''
        count = 0
        for music in items:
            s += str(music) + '\n'
        return s
    def __str__(self) -> str:
        return f"""
Total Duration: {0}
Shuffled : {0}

Music:
{self.__loadQueue()}

Page {self.__PaginationCount}/{self.__PaginationLimit}
"""

q = Queue([1,2,3,4,5,6,7,8,9,10], by=2)
q.next()
print(q)