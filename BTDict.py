
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

    def _insert_recursive(self,data,node):
        if data["id"] < node.val["id"]:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        elif data["id"] > node.val["id"]:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)
        else:
            return
    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value,self.root)
            



    def _search_recursive(self, blog_post_id, node):

        if blog_post_id == node.val["id"]:
            return node.val

        if blog_post_id < node.val["id"] and node.left is not None:
            return self._search_recursive(blog_post_id, node.left)

        if blog_post_id > node.val["id"] and node.right is not None:
            return self._search_recursive(blog_post_id, node.right)

        return False

    def search(self, blog_post_id):
        blog_post_id = int(blog_post_id)
        if self.root is None:
            return False

        return self._search_recursive(blog_post_id, self.root)
        

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

b = BinarySearchTree()

