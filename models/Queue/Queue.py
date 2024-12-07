import sys
sys.path.append("models\\")
sys.path.append("models\\track\\")
import random
from track import Track, timedelta
from pagination import Pagination
from arraylist import ArrayList
class Queue:
    """
    A class to represent a queue for managing a collection of tracks.

    Attributes:
        __totalDuration (Duration): The total duration of all tracks in the queue.
        __array (list): The list of tracks in the queue.
        __size (int): The current number of tracks in the queue.
        __itemCount (int): The maximum number of items to display per page.
        pagination (Pagination): The pagination object for managing track display.
        __shuffle (bool): Indicates whether the queue is shuffled.
        __onRepeat (bool): Indicates whether the queue is set to repeat.
        __onPause (bool): Indicates whether the playback is paused.
        __currentTrack (int): The index of the currently playing track.
        __endPage (int): The index for the end of the current page in pagination.
    """
    def __init__(self, arraylist:ArrayList, itemCount:int = 10):
        """
        Initializes the Queue object with a list of tracks and item count.

        Args:
            array (list): The list of tracks to be managed by the queue.
            itemCount (int, optional): The number of items to display per page. Defaults to 10.
        """
        self.__totalDuration = timedelta(seconds=0)
        self.__array = arraylist.getArrayList()
        self.__size = arraylist.getSize()
        self.__itemCount = itemCount
        self.pagination = Pagination(self.__size, self.__itemCount)
        self.__shuffle = False
        self.__onRepeat = False
        self.__onPause = False
        self.__currentTrack = 0
        self.__endPage = self.__setEndPage()
    
    def isonRepeat(self):
        return self.__onRepeat
    
    def isonPause(self):
        return self.__onPause
    
    def isShuffled(self):
        return self.__shuffle
    
    def totalDuration(self):
        """
        Returns the total duration of all tracks in the queue.

        Returns:
            Duration: The total duration of tracks.
        """
        return self.__totalDuration

    def getCurrentTrack(self):
        """
        Retrieves the currently playing track.

        Returns:
            Track: The track currently being played.
        """
        try:
            return self.getTrackbyIndex(self.__currentTrack)
        except IndexError:
            return None
        
    def isEmpty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.__size == 0

    def pause(self, state:bool = True)-> bool:
        """
        Pauses or resumes the playback.

        Args:
            state (bool, optional): The state to set (True for pause, False for play). Defaults to True.

        Returns:
            bool: The current pause state.
        """
        assert type(state) is bool, f"'{state}' is not a boolean value"
        self.__onPause = state
    
    def shuffle(self, state:bool = True):
        """
        Enables or disables shuffling of the queue.

        Args:
            state (bool): The state to set (True to shuffle, False to not shuffle).
        """
        assert type(state) is bool, f"'{state}' is not a boolean value"
        self.__shuffledArray = self.__array 
        random.shuffle(self.__shuffledArray)
        self.__shuffle = state

    def onRepeat(self, state:bool = True)-> None:
        """
        Sets the repeat state of the queue.

        Args:
            state (bool): The state to set (True to repeat, False to not repeat).
        """
        assert type(state) is bool, f"'{state}' is not a boolean value"
        self.__onRepeat = state

    def next(self):
        """
        Advances to the next track in the queue.
        """
        if self.__currentTrack < self.__size:
            self.__currentTrack += 1
            self.__size -= 1
            self.__endPage += 1
            self.pagination.setArraySize(self.__size)
        else:
            if self.__onRepeat:
                self.__currentTrack = 0
                self.__endPage = self.__setEndPage()
                self.pagination.setArraySize(self.__size)

    def previous(self):
        """
        Goes back to the previous track in the queue.
        """
        if self.__currentTrack > 0:
            self.__currentTrack -= 1
            self.__endPage -= 1
            self.pagination.setArraySize(self.__size)
            # self.__totalDuration.addDuration(self.getCurrentTrack().getDuration())

    def currentPage(self):
        """
        Retrieves the current page of tracks based on pagination settings.

        Returns:
            list: A list of tracks on the current page.
        """
        if self.__shuffle:
            current = self.__shuffledArray[self.__currentTrack + 1: self.__endPage] 
        else:
            current = self.__array[self.__currentTrack + 1: self.__endPage]
        return current

    def getTrackbyIndex(self, index:int)-> Track:
        """
        Retrieves a track from the queue by its index.

        Args:
            index (int): The index of the track to retrieve.

        Returns:
            Track: The track at the specified index.

        Raises:
            AssertionError: If the index is out of bounds.
        """
        return self.__array[index]
    
    def __setEndPage(self):
        """
        Sets the end page index based on the current size of the queue.
        """
        if self.__size >= self.__itemCount:
            return self.__itemCount + 1
        else:
            return self.__size
    
    def __loadPage(self)-> None:
        """
        Loads the current page of tracks and formats them as a string.
        """
        count = 0
        s = ''
        for music in self.currentPage():
            count += 1
            s += f"({count})\t{str(music)}\n"
        return s

    def __str__(self) -> str:
        """
        Returns a string representation of the queue's current state.

        Returns:
            str: A formatted string representing the queue.
        """
        banner = """
==============================
            QUEUE
=============================="""

        return banner+f"""
Total Duration: {Track.formatduration(self.__totalDuration, 'display')}
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