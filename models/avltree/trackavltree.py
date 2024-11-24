import sys
sys.path.append("models\\track\\")
sys.path.append("models\\")
from track import *
from avltree import AVLTree
import Queue
from abc import ABC, abstractmethod
from node import Node
class TrackAVLTree(AVLTree, ABC):
    def __init__(self):
        super().__init__()
        self.pagination = Queue.Pagination(self.getSize())
    
    def insert(self, track:Track):
        self.root = self.__insert(self.root, track)
        self.__incrSize()
        self.pagination.setArraySize(self.getSize())

    def __insert(self, root:Node, track:Track):
        if not root:
            return Node(track)
        result = self.compare(root.value, track)

        match result:
            case 1:
                root.left = self.__insert(root.left, track)
            case -1:
                root.right = self.__insert(root.right, track)
        return root
    
    @abstractmethod
    def compare(self, t1:Track, t2:Track, by:str="title"):
        pass

    @staticmethod
    def _compareValues(value1, value2):
        if value1 > value2:
            return 1
        elif value1 < value2:
            return -1
        else:
            return 0
    
    def currentPage(self)-> list[Track]:
        current =  self.inorder(self.root).getArrayList()
        return current[self.pagination.getStartIndex(): self.pagination.getEndIndex()]

    def loadPage(self):
        s = ''
        for track in self.currentPage():
            s += f"{str(track)}\n"
        
        return s

t1 = Track('Blinding Lights', 'The Weeknd', 'After Hours', Duration(minute=3, sec=20))
t2 = Track('Watermelon Sugar', 'Harry Styles', 'Fine Line', Duration(minute=2, sec=6))
t3 = Track('Levitating', 'Dua Lipa', 'Future Nostalgia', Duration(minute=3, sec=23))
t4 = Track('Shape of You', 'Ed Sheeran', '÷ (Divide)', Duration(minute=4, sec=23))
t5 = Track('Good 4 U', 'Olivia Rodrigo', 'SOUR', Duration(minute=3, sec=14))
t6 = Track('Stay', 'The Kid LAROI & Justin Bieber', 'F*CK LOVE 3: OVER YOU', Duration(minute=2, sec=35))
t7 = Track('Peaches', 'Justin Bieber', 'Justice', Duration(minute=3, sec=17))
t8 = Track('Kiss Me More', 'Doja Cat feat. SZA', 'Planet Her', Duration(minute=3, sec=24))
t9 = Track('Save Your Tears', 'The Weeknd', 'After Hours', Duration(minute=3, sec=35))
t10 = Track('Montero (Call Me By Your Name)', 'Lil Nas X', 'Montero', Duration(minute=2, sec=17))
# m.insert(t1)
# m.insert(t2)
# m.insert(t3)
# m.insert(t4)
# m.insert(t5)
# m.insert(t6)
# m.insert(t7)
# m.insert(t8)
# m.insert(t9)
# print(m)