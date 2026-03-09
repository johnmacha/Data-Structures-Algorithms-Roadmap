class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node= Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def print(self):
        if self.head == None:
            print("List is empty")
            return
        
        llstr = ''
        itr = self.head
        while itr:
            llstr += str(itr.data) + '<->'
            itr = itr.next

        llstr += "None"
        print(llstr)

if __name__ == '__main__':
    ll = Linkedlist()
    ll.insert_at_start(10)
    ll.insert_at_start(17)
    ll.insert_at_end(27)
    ll.print()

