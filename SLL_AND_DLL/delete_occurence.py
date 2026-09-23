#DELETE OCCURENCES OF A KEY
# Structure of the doubly linked list Node 
# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.prev = None

class Solution:
    def deleteAllOccurOfX(self, head, x):
        curr = head

        while curr:
            if curr.data == x:

                # If deleting head
                if curr == head:
                    head = curr.next

                # Connect previous node
                if curr.prev:
                    curr.prev.next = curr.next

                # Connect next node
                if curr.next:
                    curr.next.prev = curr.prev

            curr = curr.next

        return head