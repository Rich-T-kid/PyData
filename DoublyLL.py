class Node:
    def __init__(self,data,next=None,prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None


    def addHead(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
           x = self.head
           x.prev = node
           node.next = x
           node.prev = None
           self.head = node

        
    
    def AddEnd(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = None
            node.prev = None
            return
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
            node.prev = current
            node.next = None
    
    def DeleteNode(self,element):
        found = False
        current = self.head
        while current:
            if current.data == element:
                found = True
                hold = current.prev
                hold1 =  current.next
                hold.next = hold1
                hold1.prev = hold
                current.prev = None
                current.next = None
                print(f"removed {element}")
            current = current.next
        if found == False:
            print(f"element: {element} doesnt exist in table")


    def PrintLL(self):
        node = self.head
        while node:
            print(node.data,end="-> ")
            node = node.next
        print("none")
l = DoublyLinkedList()