#REVERSE DOUBLY LINKED LIST
""" Structure of Doubly Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        if head.next is None:
            return head
        current=head
        prev=None
        
        while current is not None:
            front=current.next
            current.next=prev
            current.prev=front
            prev=current
            current=front
        return prev