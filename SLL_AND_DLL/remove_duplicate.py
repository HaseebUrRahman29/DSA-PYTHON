#REMOVE DUPLICATES
# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None

class Solution:
    def removeDuplicates(self, headRef):
        curr = headRef

        while curr is not None and curr.next is not None:
            if curr.data == curr.next.data:
                curr.next = curr.next.next

                if curr.next is not None:
                    curr.next.prev = curr
            else:
                curr = curr.next

        return headRef