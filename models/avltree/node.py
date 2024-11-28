class Node:
    def __init__(self, value):
        self.value = value
        self.left:Node = None
        self.right:Node = None
        self.height = 1
    
    def __repr__(self) -> str:
        return repr(self.value)