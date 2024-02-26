class Queue:
    def __init__(self):
        self.queue = []

    def _queuelen(self) -> int:
        return len(self.queue)

    def enqueue(self,item):
        if self.isFull() is False:
            self.queue.append(item)
        else:
            return " queue is full "

    def dequeue(self):
         if self.IsEmpty != True:
           # self.queue.pop(0)
            return self.queue.pop(0)
         else:
             return "queue is empty"

    def peak(self):
        return self.queue[0]
    
    def isFull(self):
        if self._queuelen() >= 10000:
            return True
        return False
    
    def IsEmpty(self) -> bool:
        if self._queuelen() == 0:
            return True
        else:
            return False

B = Queue()
B.enqueue(4)
B.enqueue(5)
print(B.dequeue())
print(B.dequeue())
