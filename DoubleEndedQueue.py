from collections import deque

class DoubleEndedQueue:
    def __init__(self):
        self.queue = deque()

    def first(self):
        if not self.queue:
            raise IndexError("Deque is empty")
        return self.queue[0]
    
    def last(self):
        if not self.queue:
            raise IndexError("Deque is empty")
        return self.queue[-1]
    
    def pushFront(self, item):
        self.queue.appendleft(item)
    
    def pushBack(self, item):
        self.queue.append(item)
    
    def popFront(self):
        if not self.queue:
            raise IndexError("Deque is empty")
        return self.queue.popleft()
    
    def popBack(self):
        if not self.queue:
            raise IndexError("Deque is empty")
        return self.queue.pop()
