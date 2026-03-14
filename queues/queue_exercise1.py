#Multithreading in Python
import time
import threading
from collections import deque

class Queue():
    def __init__(self):
        self.order = deque()
    
    def enqueue(self, val):
        self.order.appendleft(val)
    
    def dequeue(self):
        return self.order.pop()
    
    def is_empty(self):
        return len(self.order)==0
    
    def size(self):
        return len(self.order)

orders = ['pizza','samosa','pasta','biryani','burger']
q = Queue()
def place_order(p):
    for o in p:
        q.enqueue(o)
        print('Placing order :',place_order(o))
        time.sleep(0.5)


def serve_order():
    time.sleep(1) #Also start this thread 1 second after place order thread is started.
    for i in range(len(orders)):
        order = q.dequeue()
        print("Now serving: ",order)
        time.sleep(2)
        # print(serve_order())

t1 = threading.Thread(target = place_order,args=(orders,))
t2 = threading.Thread(target = serve_order)

t = time.time()
t1.start()
time.sleep(1)
t2.start()

t1.join()
t2.join()

print('process done in :',time.time()-t)
