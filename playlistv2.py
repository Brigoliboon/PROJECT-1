from datetime import datetime
from models.Playlist.track import Track
import json

class Node:
    def __init__(self, value:Track):
        assert type(value) is Track, 'Incorrect given value. value must be a Track type'
        self.__value:Track = value
        self.__right:Node = None
        self.__left:Node = None
    
    def getValue(self):
        return self.__value
    
    def setValue(self, value):
        self.__value = value

    def getRight(self):
        return self.__right
    
    def setRight(self, value):
        self.__right = value
    
    def getLeft(self):
        return self.__left
    
    def setLeft(self, value):
        self.__left = value
    
    def __str__(self) -> str:
        return str(self.__value)
    
    def __repr__(self) -> str:
        return str(self.__value)

class PlayList: 
    def __init__(self, title:str = None):
        self.__title = title
        self.__creationDate:datetime = datetime.today()
        self.__root:Node = None

    def getRoot(self):
        return self.__root
    
    def getTitle(self):
        return self.__title
    
    def getCreationDate(self):
        return self.__creationDate

    def insert(self, value:Track):
        if self.__root is None:
            self.__root = Node(value)
        else:
            self.__nodeInsertion(value, self.getRoot())

    def search(self, value:str, by:str = None, node:Node = None):
        if node is None:
            return self.search(value, node=self.getRoot(), by=by)
        else:
            if value > self.__getattribute__(by):
                return 
    
    def __nodeInsertion(self, value:Track, node:Node = None):
        if node is None:
            return self.__nodeInsertion(value, self.getRoot())
        if value.getTitle() < node.getValue().getTitle():
            if node.getLeft() is None:
                node.setLeft(Node(value))
            else:
                self.__nodeInsertion(value, node.getLeft())
        else:
            if node.getRight() is None:
                node.setRight(Node(value))
            else:
                self.__nodeInsertion(value, node.getRight())
    
    # @staticmethod
    # def __compareNodeValues(value, node:Node, recursiveFunction:function, by:str = 'title'):
    #     if value > getattr(node, by):
    #         return recursiveFunction(value, node.getRight())
    #     elif value < getattr(node, by):
    #         return recursiveFunction(value, node.getLeft())

    def print_tree(self, node:Node, level=0):
        if node is not None:
            self.print_tree(node.getRight(), level + 1)
            print(' ' * 4 * level + '-> ' + str(node.getValue()))
            self.print_tree(node.getLeft(), level + 1)
    
    def to_dict(self, node:Node):
        """Convert the binary tree to a dictionary."""
        if node is None:
            return None
        return {
            'value': node.getValue().getTitle(),
            'left': self.to_dict(node.getLeft()),
            'right': self.to_dict(node.getRight())
        }

    def to_json(self):
        """Convert the binary tree to a JSON string."""
        tree_dict = self.to_dict(self.getRoot())
        return json.dumps(tree_dict)