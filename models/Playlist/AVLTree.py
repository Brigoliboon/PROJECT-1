from arraylist import ArrayList
class Node:
    def __init__(self, value):
        self.value = value
        self.left:Node = None
        self.right:Node = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
        self.__size = 0

    def getRoot(self):
        return self.root
    
    def getSize(self):
        return self.__size

    def height(self, node:Node):
        if not node:
            return 0
        return node.height

    def balance(self, node:Node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def __insert(self, root:Node, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.__insert(root.left, value)
        else:
            root.right = self.__insert(root.right, value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

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

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z:Node):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, z:Node):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def min_value_node(self, root:Node):
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

    def insert(self, value):
        self.root = self.__insert(self.root, value)
        self.__size +=1

    def delete_value(self, value):
        self.root = self.delete(self.root, value)

    def search(self, value):
        return self.__search(self.root, value)
    
    def inorder(self, root:Node)-> list:
        # Inorder traversal (Left, Root, Right)
        inorder = []
        if root:
            self.inorder(root.left)
            inorder.append(root)
            self.inorder(root.right)
        
        return inorder
    def preorder(self, root:Node):
        # Preorder traversal (Root, Left, Right)
        if root:
            print(root.value, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root:Node):
        # Postorder traversal (Left, Right, Root)
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value, end=" ")
