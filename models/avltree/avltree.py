import sys
sys.path.append("models\\")
sys.path.append("models\\Queue")
from abc import ABC, abstractmethod
from Queue import ArrayList
from .node import Node

class AVLTree(ABC):
    def __init__(self):
        self.root = None
        self.__size = 0
        self.__reservedMemory = ArrayList()

    def getRoot(self):
        return self.root
    
    def getSize(self):
        return self.__size
    
    def incrSize(self):
        self.__size += 1
    
    def height(self, node:Node):
        if not node:
            return 0
        return node.height

    def __balance(self, node:Node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def insert(self, value):
        self.root = self.__insert(self.root, value)
        self.__incrSize()

    def __insert(self, root:Node, value):
        if not root:
            return Node(value)

        elif value < root.value:
            root.left = self.__insert(root.left, value)
            
        elif value > root.value:
            root.right = self.__insert(root.right, value)

        elif value == root.value:
            return (root, 'equal')
        
        self.__check_balance(root, value)
        return root

    def __check_balance(self, root:Node, value):
        
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.__balance(root)
        # Left rotation
        if balance > 1 and value < root.left.value:
            return self.__right_rotate(root)

        # Right rotation
        if balance < -1 and value > root.right.value:
            return self.__left_rotate(root)

        # Left-Right rotation
        if balance > 1 and value > root.left.value:
            root.left = self.__left_rotate(root.left)
            return self.__right_rotate(root)

        # Right-Left rotation
        if balance < -1 and value < root.right.value:
            root.right = self.__right_rotate(root.right)
            return self.__left_rotate(root)

    def delete(self, root:Node, value):
        if not root:
            return root

        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.__min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.__balance(root)

        # Left rotation
        if balance > 1 and self.__balance(root.left) >= 0:
            return self.__right_rotate(root)

        # Right rotation
        if balance < -1 and self.__balance(root.right) <= 0:
            return self.__left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.__balance(root.left) < 0:
            root.left = self.__left_rotate(root.left)
            return self.__right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.__balance(root.right) > 0:
            root.right = self.__right_rotate(root.right)
            return self.__left_rotate(root)

        return root

    def __left_rotate(self, z:Node):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def __right_rotate(self, z:Node):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def __min_value_node(self, root:Node):
        current = root
        while current.left:
            current = current.left
        return current

    def __search(self, root:Node, value):
        if not root or root.value == value:
            return root
        if root.value < value:
            return self.__search(root.right, value)
        return self.__search(root.left, value)
        
    def delete_value(self, value):
        self.root = self.delete(self.root, value)

    def search(self, value):
        return self.__search(self.root, value)
    
    def inorder(self, root:Node):
        # Inorder traversal (Left, Root, Right)
        if root:
            self.inorder(root.left)
            self.__reservedMemory.insert(root.value)
            self.inorder(root.right)
        return self.__reservedMemory
    def preorder(self, root:Node):
        # Preorder traversal (Root, Left, Right)
        arraylist = ArrayList(size=self.__size)
        if root:
            arraylist.insert(root.value)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root:Node):
        # Postorder traversal (Left, Right, Root)
        arraylist = ArrayList(size=self.__size)
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            arraylist.insert(root.value)
        return arraylist

# avl = AVLTree()
# s1 = 2
# s2 = 1
# avl.insert(s1)
# avl.insert(s2)
# # # t1 = Track("Blinding Lights", "The Weeknd", "After Hours", Duration(0, 20, 30))
# # # t2 = Track("Watermelon Sugar", "Harry Styles", "Fine Line", Duration(0, 20, 2))
# # avl.insert(t1)
# # avl.insert(t2)
# print(avl.inorder(avl.root))