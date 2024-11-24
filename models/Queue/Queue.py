import sys
sys.path.append("models\\")
sys.path.append("models\\track\\")
import random
from track import Track, Duration
from pagination import Pagination
class Queue:
    def __init__(self, array:list, itemCount:int = 10):
        self.__totalDuration = Duration(3, 20, 10)

        self.__array = array
        self.__size = len(self.__array)
        self.__itemCount = itemCount
        self.pagination = Pagination(self.__size, 10)
        self.__shuffle = False
        self.__onRepeat = False
        self.__onPause = False
        self.__currentTrack = 0
        self.__endPage = self.__setEndPage()
    
    def totalDuration(self):
        return self.__totalDuration

    def getCurrentTrack(self):
        return self.getTrackbyIndex(self.__currentTrack)
    
    def isEmpty(self):
        return self.__size == 0

    def pause(self, state:bool = True)-> bool:
        assert type(state) is bool, f"'{state}' is not a boolean value"
        self.__onPause = state
    
    def shuffle(self, state:bool = True):
        assert type(state) is bool, f"'{state}' is not a boolean value"
        self.__shuffledArray = self.__array 
        random.shuffle(self.__shuffledArray)
        self.__shuffle = state

    def onRepeat(self, state:bool = True)-> None:
        assert type(state) is bool, f"'{state}' is not a boolean value"
        self.__onRepeat = state

    def next(self):
        if self.__currentTrack < len(self.__array)-1:
            self.__currentTrack += 1
            self.__size -= 1
            self.__endPage += 1
            self.pagination.setArraySize(self.__size)
        else:
            if self.__onRepeat:
                self.__currentTrack = 0
                self.__size  = len(self.__array)
                self.__endPage = self.__setEndPage()
                self.pagination.setArraySize(self.__size)

    def previous(self):
        if self.__currentTrack > 0:
            self.__currentTrack -= 1
            self.__endPage -= 1
            self.__size += 1
            self.pagination.setArraySize(self.__size)
            # self.__totalDuration.addDuration(self.getCurrentTrack().getDuration())

    def currentPage(self):
        if self.__shuffle:
            current = self.__shuffledArray[self.__currentTrack + 1: self.__endPage] 
        else:
            current = self.__array[self.__currentTrack + 1: self.__endPage]
        return current

    def getTrackbyIndex(self, index:int)-> Track:
        assert index >=0 and index < self.__size, "Index out of bounds."
        return self.__array[index]
    
    def __setEndPage(self):
        if self.__size >= self.__itemCount:
            return self.__itemCount + 1
        else:
            return self.__size
    
    def __loadPage(self)-> None:
        count = 0
        s = ''
        for music in self.currentPage():
            count += 1
            s += f"[{count}]\t{str(music)}\n"
        return s

    def __str__(self) -> str:
        if self.isEmpty():
            return "Empty Playlist"
        else:
            return f"""
Total Duration: {self.__totalDuration.getHour()} hr {self.__totalDuration.getMinute()} min
Shuffled: {"Yes" if self.__shuffle else "No"}
Repeat: {"Yes" if self.__onRepeat else "No"}
Tracks:
    Currently playing{' (Paused)' if self.__onPause else ''}:
        {self.getCurrentTrack()}
Next: 
{self.__loadPage()}
{str(self.pagination)}"""


# l = [1]
# q = Queue(l)
# print(q)
# p = Pagination(len(l), 10)
# p.next()
# p.next()
# p.previous()
# p.previous()
# start = p.getStartIndex()
# end = p.getEndIndex()
# print(f"[{start}:{end}]")
# print(f"{p.page_count}/{p.page_limit} Pages")
# print(l[start:end])

# q = Queue([1,2,3])
# q.totalDuration().addDuration(Duration(hour=0, minute=4, sec= 0))
# q.totalDuration().addDuration(Duration(hour=0, minute=5, sec= 0))
# q.onRepeat(True)
# q.shuffle(True)

# q.next()
# q.previous()
# q.previous()

# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()
# q.next()

# while True:
#     print(q)
#     p = input("function: ")
#     if p == 'n':
#         q.next()
#     if p == 'p':
#         q.previous()
#     print(q)
#     if p == 's':
#         q.shuffle()
#     if p == 'r':
#         q.onRepeat()
#     if p == 'e':
#         break
#     if p == 'pa':
#         q.pause()