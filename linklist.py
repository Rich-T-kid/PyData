class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = None
 
# implement as doubly linked list later
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def to_list(self):
        l = []
        if self.head is None:
            return l
        
        current = self.head
        while current:
            l.append(current.data)
            current = current.next
        return l
    def addHead(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def addNode(self,data):
        node = Node(data,next=None)
        if self.head is None:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node
        self.tail = node

    def PrintLL(self):
        node = self.head
        while node != None:
            print(node.data,end="-> ")
            node = node.next
        print("none")

    def Contains(self,data):
        start = self.head
        while start.next:
            if start.data == data:
                return True
            else:
                start = start.next
        return False

    def deleteNode(self,data):
        if self.head is None:
            return "empty linked list"
        if self.head.data == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return f"deleted node {data}"
        current = self.head
        while current.next:
            if current.next.data == data:
                if current.next == self.tail:
                 self.tail = current
                current.next = current.next.next
                # may want to implement deleting memory and overhead of node object instead of just moving pointers around later if needed
                return f"deleted node {data}"
            current = current.next
        return "node was not found"


    def insertend(self,data):
        node = Node(data)
        self.tail.next = node


    def reverselinked(self):
       prev = None
       current = self.head
       while current is not  None:
           next = current.next
           current.next = prev
           prev = current
           current = next
       self.head = prev
       return prev
    
    def Printfromhead(self,head):
        node = head
        while node != None:
            print(node.data,end="-> ")
            node = node.next
        print("none")

    def combine(self,head1,head2):
        tail = head1
        current =  head1.next
        current2 = head2
        head1.next = head2
        count = 0
        while current is not None and current2 is not None:
          if count % 2 == 0:
              tail.next = current2
              current2 = current2.next
          else:
              tail.next = current
              current = current.next
          tail = tail.next
          count += 1
        if current2 is not None:
            tail.next = current2
        elif current is not None:
            tail.next = current
        tail.next = None
    
        return head1
    def head(self):
        return self.head
          
"""   
l = LinkedList()

l.addHead(2)
l.addNode(32)
l.insertend(21)
l.addNode(9442)
l.addNode(323)
l.addNode(976)
l.addNode(323)
l.addHead(12)
"""

