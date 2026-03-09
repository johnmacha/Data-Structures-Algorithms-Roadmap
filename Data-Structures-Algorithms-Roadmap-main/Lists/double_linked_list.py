class Node:
    def __init__(self, data=None, prev=None, next=None ):
        self.data = data
        self.prev = prev
        self.next = next

class Linkedlist:
    def __init__(self):
       self.head = None
           
    def print_forward(self):
        #This method prints list in forward direction. Use node.next
        if self.head is None:
            print("Empty list")
            return
        
        node = self.head
        llstr = ''
        while node:
            llstr += str(node.data) + '<->'
            node = node.next

        llstr += "None"    
        print(llstr)
    
    def print_backward(self):
        #Print linked list in reverse direction. Use node.prev
        if self.head is None:
            print("List is empty!")
            return
        
        #go to the last node
        node = self.head
        while node.next:
            node = node.next

        #now print backwards
        llstr = ''
        while node:
            llstr += str(node.data) + '<->'
            node = node.prev
        
        llstr += "None"
        print(llstr)
    
    def debug_prev(self):
        node = self.head
        while node:
            print(f"Node={node.data}, Prev={node.prev.data if node.prev else None}")
            node = node.next


    def insert_at_start(self, data):
        new_node = Node(data, prev=None, next=self.head)

        if self.head:
            self.head.prev = new_node

        self.head = new_node
            
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        
        itr = self.head #traversal
        while itr.next:
            itr = itr.next
            

        new_node = Node(data, itr, None)
        itr.next = new_node

    def insert_at(self, newdata, data_insert):
        if self.head is None:
         return
    
        itr = self.head
        while itr:
            if itr.data == newdata :
                node = Node(data_insert, prev=itr, next=itr.next)

                if itr.next:
                    itr.next.prev = node

                itr.next = node 
                return
            
            itr = itr.next
            
if __name__ == '__main__':
    ll = Linkedlist()
    ll.insert_at_start(6)
    ll.insert_at_start(4)
    ll.insert_at_start(5)
    ll.insert_at(6, 9)
    ll.insert_at_end(2)
    ll.print_forward()
    ll.debug_prev()
    ll.print_backward()
    
    