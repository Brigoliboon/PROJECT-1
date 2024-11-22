class Queue:
    def __init__(self, array:list, itemCount:int = 10):
        self.__array = array
        self.__size = len(self.__array)
        self.__itemCount = itemCount
        self.__currentTrack = 0
        self.__endPage = self.__setEndPage()
        self.__setPaginationLimit()

    def getCurrentTrack(self):
        return self.getTrackbyIndex(self.__currentTrack)
    
    def getPaginationLimit(self):
        return self.__PaginationLimit
    
    def __setEndPage(self):
        if self.__size >= self.__itemCount:
            return self.__itemCount + 1
        else:
            return self.__size

    def next(self):
        if self.__currentTrack < len(self.__array):
            self.__currentTrack += 1
            self.__endPage += 1
            self.__size -= 1
        else:
            if self.onre
    def previous(self):
        if self.__currentTrack > 0:
            self.__currentTrack -= 1
            self.__endPage -= 1
            self.__size += 1

    def currentPage(self):
        return self.__array[self.__currentTrack + 1: self.__endPage]
    

    def getTrackbyIndex(self, index:int):
        return self.__array[index]
    
    def __setPaginationLimit(self)-> None:
        self.__remainder = self.__size % 10 if self.__size/10 >= 1 else 0
        self.__PaginationLimit = 1 if int(self.__size//10) < 1 else int(self.__size//10)
        if self.__remainder:
            self.__PaginationLimit += 1
    
    def __loadPage(self)-> None:
        self.__setPaginationLimit()
        count = 0
        s = ''
        for music in self.currentPage():
            count += 1
            s += f"[{count}] {str(music)}\n"
        return s

    def __str__(self) -> str:
        return f"Current Track: {self.getCurrentTrack()}\nMusic\n{self.__loadPage()}\nPagination: {self.__PaginationLimit} Pages"

# q = Queue([1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,])
q = Queue([1])

# print(q.getCurrentTrack())
# print(q.currentPage())
# print('limit: ', q.getPaginationLimit())
print(q)