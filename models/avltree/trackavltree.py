import sys
sys.path.append("models\\track\\")
sys.path.append("models\\")
from .avltree import AVLTree
from track import *
from Queue import *
from abc import ABC, abstractmethod
from .node import Node

class TrackAVLTree(AVLTree):
    """
    A TrackAVLTree is an extension of the AVLTree that manages a collection of Track objects.
    It provides functionality for inserting tracks, creating a playback queue, 
    and paginating through the tracks.
    """
    def __init__(self):
        """
        Initializes a new instance of TrackAVLTree.
        Sets up the AVL Tree structure and initializes pagination and queue.
        """
        super().__init__()
        self.pagination = Pagination(self.getSize())
        self.__queue = None
    

    def getQueue(self):
        """
        Retrieves the current playback queue.

        Returns:
            Queue: The queue containing the tracks.
        """
        if not self.__queue:
            self.play()
        return self.__queue

    def play(self):
        """
        Prepares the playback queue by creating it from the current set of tracks.
        """
        if not self.__queue:
            self.createQueue()
    def stop(self):
        self.__queue = None

    def insert(self, track:Track):
        """
        Inserts a new track into the AVL Tree and updates the pagination size.

        Args:
            track (Track): The Track object to be inserted into the tree.
        """
        
        self.root = self.__insert(self.root, track)
        self.incrSize()
        self.pagination.setArraySize(self.getSize())

    def __insert(self, root:Node, track:Track):
        """
        Helper method to insert a track into the AVL Tree recursively.

        Args:
            root (Node): The root node of the subtree.
            track (Track): The Track object to be inserted.

        Returns:
            Node: The updated root node of the subtree.
        """
        if not root:
            return Node(track)
        result = self.compare(root.value, track)

        match result:
            case 1:
                root.left = self.__insert(root.left, track)
            case -1:
                root.right = self.__insert(root.right, track)
        return root
    
    def createQueue(self):
        """
        Creates a playback queue by performing an inorder traversal of the AVL Tree
        and populating the queue with the tracks.
        """
        array = self.inorder(self.root)
        self.__queue = Queue(array)

    @abstractmethod
    def compare(self, t1:Track, t2:Track, by:str="title"):
        """
        Abstract method for comparing two Track objects.

        Args:
            t1 (Track): The first Track object to compare.
            t2 (Track): The second Track object to compare.
            by (str): The attribute to compare by (default is "title").

        Returns:
            int: A comparison result; 1 if t1 > t2, -1 if t1 < t2, 0 if equal.
        """
        pass

    @staticmethod
    def _compareValues(value1, value2):
        """
        Compares two values and returns the comparison result.

        Args:
            value1: The first value to compare.
            value2: The second value to compare.

        Returns:
            int: 1 if value1 > value2, -1 if value1 < value2, 0 if equal.
        """
        if value1 > value2:
            return 1
        elif value1 < value2:
            return -1
        else:
            return 0
    
    def currentPage(self)-> list[Track]:
        """
        Retrieves the current page of tracks based on pagination settings.

        Returns:
            list[Track]: A list of Track objects on the current page.
        """
        current =  self.inorder(self.root).getArrayList()
        return current[self.pagination.getStartIndex(): self.pagination.getEndIndex()]

    def loadPage(self, counter:bool = False):
        """
        Loads the current page of tracks and formats them for display.

        Args:
            counter (bool): If True, includes a counter in the display format.

        Returns:
            str: A formatted string of the current page of tracks.
        """
        s = ''
        count = 0
        for track in self.currentPage():
            if counter:
                count +=1
                s += f"[{count}] {str(track)}\n"
            else:
                s += f"{str(track)}\n"
        return s