class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
        

    def is_empty(self):
        return True if self.stack == 0 else False