import Stack
from  queue import Queue

class Node:
    def __init__(self,val=None) -> None:
        self.val= val
        self.left = None
        self.right = None
    

class BinarySearchTree:
    def __init__(self) :
        self.root = None
    
    def rootval(self):
        return self.root.val

    def _insert_recursive(self,value,root):
        if value < root.val:
            if root.left is None:
                root.left = Node(value)
            else:
                self._insert_recursive(value,root.left)
        if value > root.val:
            if root.right is None:
                root.right = Node(value)
            else:
                self._insert_recursive(value,root.right)
        else:
            return "already exist in tree"
    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value,self.root)
            



    def search(self,value,root):
        if root is None:
            return "doesnt exist in tree"
        if root.val == value:
            return root.val
        if value < root.val:
            return self.search(value,root.left)
        if value > root.val:
            return self.search(value,root.right)

        

    def getMin(self):
        start= self.root
        while start is not None:
            start = start.left
        least = start
        return least

    def getMax(self):
        start = self.root
        while start is not None:
            start = start.right
        most = start
        return most

    def delete(self,node):
        if self.search(node) != "doesnt exist in tree":
        # three base cases
        # the node to delete has no children
        # the node to delete has 1 child
        # the node to delete has 2 children
            pass

    def exist(self,node):
        if self.search(node) !=  "doesnt exist in tree":
            return True
        else:
            return False
    


    def inorder(self,root):
       if root:
           self.inorder(root.left)
           print(str(root.val))
           self.inorder(root.right)


    def preorder(self,root):
        if root:
            print(str(root.val))
            self.preorder(root.left)
            self.preorder(root.right)
        

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(str(root.val))

# pre order depth first traversal
    def DFS(self,root):
        if root is None:
            return []
        answer = []
        s = Stack.Stack()
        s.push(root)
        while s.isempty() != True:
           current = s.pop()
           answer.append(current)

           # goes left to right
           if current.right is not None:
               s.push(current.right)
           if current.left is not None:
               s.push(current.left)
        return answer

# recursive implentation of Depth first search
    def DFSR(self,root):
        if root is None:
            return 
        left = self.DFSR(root.left)
        right = self.DFSR(root.right)

        return [root.value] + left + right
       


    def BFS(self,root):
        if root is None:
            return []      
        final  = []                                                   
        q =  Queue()
        q.enqueue(root) 
        while q._queuelen() > 0:   
            current = q.peak()                                              
            if current.left is not None:                                              
                q.enqueue(current.left)
            if current.right is not None:                                              
                q.enqueue(current.right)
            final.append(current)
            q.dequeue()
        return final

    # recursive approach to finding sum of binary tree
    def FindSum(self,root):
        if root is None:
            return 0

        
        leftSum = self.FindSum(root.left)
        rightSum = self.FindSum(root.right)

        total = root.val + leftSum + rightSum
        return total


    def findsumIT(self,root):
        sum = 0
        # implement later. quite triveral


    def minval(self,root):
        if root is None:
            return 0
        minv = 5342323232
        q = Queue()
        q.enqueue(root)
        while q.IsEmpty() != True:
            current = q.peak()
            minv = min(current.val,minv)
            if current.left != None:
                q.enqueue(current.left)
            if current.right != None:
                q.enqueue(current.right)
            q.dequeue()
        return minv
    
    def minvalRecursive(self,root):
        if root is None:
            return float('inf')
        
        left = self.minvalRecursive(root.left)
        right = self.minvalRecursive(root.right)

        return min(root.val,left,right)


    def maxval(self,root):
        if root is None:
            return -42323424
        
        left = self.maxval(root.left)
        right = self.maxval(root.right)

        return max(root.val,left,right)
    

    def MaxRootToLeaf(self,root):
        pass
    # generate all possible paths from root to leaf
    # find the sum of each possible path
    # return the path with the highest sum 
        
            
b = BinarySearchTree()

import random
for i in range(15):
    x = random.randrange(3,27)
    b.insert(x)
b.insert(5)
print("root value -> ",b.rootval())
