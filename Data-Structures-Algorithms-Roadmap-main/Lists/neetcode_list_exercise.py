#Reversing a singly_linked_list
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: #The 'return type' hint
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
    #Helper to create a list from python list
    def create_linked_list(self, values):
        if not values:
            return None
        
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    #Helper to print the linked list
    def print_list(self, head: ListNode) -> None:
        current = head
        while current:
            print(current.val, end=" ->")
            current = current.next
        print("None")

    #Main execution
if __name__ == "__main__":
    solution = Solution()
    
    print("Original list:")
    head = solution.create_linked_list([0,1,2,3])
    solution.print_list(head)

    print("Reversed list:")
    head = solution.reverseList(head)
    solution.print_list(head)
    