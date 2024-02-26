import random
class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right


class MaxHeap:
    def __init__(self):
        self.root = None
    
    
    def __repr__(self):
        return f"Node value={self.data})"
    
    def insert(self,data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            self._insertRecursively(data,self.root)

    def _insertRecursively(self, data, current_node):
        if data > current_node.data:
            data, current_node.data = current_node.data, data
        if current_node.left is None:
            current_node.left = Node(data)
        elif current_node.right is None:
            current_node.right = Node(data)
        else:
            # Recursively insert into the left or right subtree, favoring the left subtree
            if random.choice([True, False]):
                self._insertRecursively(data, current_node.left)
            else:
                self._insertRecursively(data, current_node.right)

    def getMax(self):
        return self.root
    

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(str(self.root))
            self.inorder(root.right)
        
    def Pop_returnROot(self):
        if self.root is None:
            return None
        if self.root.left is None:
            self.root = self.root.right
        elif self.root.right is None:
            self.root = self.root.left
        x = self.root
        if self.root.left > self.root.right:
            self.root = self.root.left
        else:
            self.root = self.root.right
        
        return x
    

b = MaxHeap()
b.insert(5)
b.inorder(b.root)


