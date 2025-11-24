#Example of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#create nodes
head = Node(10)
head.next = Node(15)
head.next.next = Node(18)

#traversal
current = head
while current is not None:
    print (current.data)
    current = current.next