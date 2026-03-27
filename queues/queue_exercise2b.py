# Method 2 for exercise_2
from collections import deque

class Queue():
    def __init__(self):
        self.buffer = deque()

    def add(self, val):
        self.buffer.append(val)
    
    def popitem(self):
        return self.buffer.popleft()
    
    def front(self):
        return self.buffer[0]# peek from the right
    
    def empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
def binary(b):
    q = Queue()

    q.add("1")
    for m in range(b):
        front = q.front()
        print(" ", front)
        q.add(front + "0")
        q.add(front + "1")

        q.popitem()

if __name__ == '__main__':
    binary(10)
