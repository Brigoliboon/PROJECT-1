import sys
sys.path.append('models\\track\\')
sys.path.append('models\\')
from track import Track
from pagination import Pagination
class ArrayList:
    """
    A class that implements a dynamic array list for storing Track objects.
    It provides methods for inserting, retrieving, and managing a list of tracks, Playlist, Music Library.
    """
    def __init__(self, size = 50) -> None:
        """
        Initializes an ArrayList with a specified initial capacity.

        Args:
            size (int): The initial capacity of the array list. Default is 50.
        """
        self.__type = type
        self.__size = 0
        self.__arraylist = [None] * size
        self.__capacity = size
        self.pagination = Pagination(self.__size)

    def getSize(self):
        """
        Returns the current number of elements in the array list.

        Returns:
            int: The size of the array list.
        """
        return self.__size
    
    def getArrayList(self) -> list[Track]:
        """
        Returns a list of Track objects currently stored in the array list.

        Returns:
            list[Track]: A list containing the Track objects.
        """
        return self.__arraylist[:self.__size]

    def isEmpty(self) -> bool:
        """
        Checks if the array list is empty.

        Returns:
            bool: True if the array list is empty, False otherwise.
        """
        return self.__size == 0
    
    def clear(self):
        """
        Clears the array list by resetting it to its initial capacity with None values.
        """
        self.__arraylist = [None] * self.__capacity

    def insert(self, value):
        """
        Inserts a Track object into the array list.

        Args:
            value (Track): The Track object to be inserted.
        """
        # assert self.__type is type(value), f"Invalid value type. must be a {self.__type}"
        if self.__size == self.__capacity:
            self.__increaseCapacity(self.__capacity)
        self.__arraylist[self.__size] = value
        self.__increaseSize()
    
    def getItemPage(self, index:int):
        assert index >= 1 and index <= 10, "Index out of bounds."
        self.getCurrentPage()[index]
    def getCurrentPage(self):
        """
        Retrieves the current page of Track objects based on pagination.

        Returns:
            list[Track]: A list of Track objects for the current page.
        """
        return self.getArrayList()[self.pagination.getStartIndex():self.pagination.getEndIndex()]
    
    # def __comparePlaylist(p1:Playlist, p2:Playlist):
    #     pass
    
    def __loadPage(self):
        """
        Loads the current page of Track objects and formats them as a string.

        Returns:
            str: A string representation of the current page of Track objects.
        """
        counter = 0
        s = ''
        for track in self.getCurrentPage():
            counter += 1
            s+= f'[{counter}] {track}'

    def __increaseSize(self):
        """
        Increases the size of the array list by one.
        """
        self.__size += 1
    
    def __increaseCapacity(self, value:int = 10):
        """
        Increases the capacity of the array list by adding more None values.

        Args:
            value (int): The number of None values to add to increase capacity. Default is 10.
        """
        self.__arraylist += [None]*value
    
    def __str__(self, format= "array") -> str:
        """
        Returns a string representation of the array list in the specified format.

        Args:
            by (str): The format of the string representation. Can be "array" or "paginate".

        Returns:
            str: A string representation of the array list.
        """
        match format:
            case "array":
                return str(self.getArrayList())
            case "paginate":
                if not self.__size:
                    return f"List is Empty...\n{self.pagination}"
                else:
                    return self.__loadPage()