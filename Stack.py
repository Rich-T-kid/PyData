class Stack:
    def __init__(self):
        self.stack = []
        
    def staklen(self):
       return len(self.stack)

    def pop(self):
        hold = self.stack.pop()
        return hold
    
    def push(self,item):
        self.stack.append(item)
    
    def staklen(self):
       return len(self.stack)
    
    def peak(self):
        x =  self.staklen()
        x -= 1
        return self.stack[x]
    
    def isempty(self) -> bool:
        if self.staklen() > 0:
            return True
        else:
            return False
        
    def isFull(self) -> bool:
        if self.staklen() >= 10000:
            return True
        return False,"finish implemeting later"



s  = Stack()
s.push(5631)
s.push(312)
s.push(323)
s.push(34)
s.push(5631)
print(s.peak())