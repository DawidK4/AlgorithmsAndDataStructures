class Queue:
    def __init__(self):
        self.q = []

    def inject(self, item):
        self.q.append(item)

    def out(self):
        return self.q.pop()
    
    def front(self):
        return self.q[-1]