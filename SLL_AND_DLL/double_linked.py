class Node():
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

class doublelinkedlist():
    def __init__(self):
        self.head=None

    def insert_at_head(self,val):
        new_node=Node(val)
        if not self.head:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node

    def append(self,val):
        new_node=Node(val)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node
            new_node.prev=current

    def insert_at(self,val,position):
        new_node=Node(val)
        if self.head is None:
            self.insert_at_head(val)
            return
        current=self.head
        count=0
        while current is not None and count<position-1:
            current=current.next
            count+=1
        if current is None:
            print("POSITION IS INVALID")
            return

        new_node.next=current.next
        new_node.prev=current
        if current.next:
            current.next.prev=new_node
        current.next=new_node

    def traverse(self):
        if self.head is None:
            print("DLL IS EMPTY")
        else:
            current=self.head
            while current is not None:
                print(current.val,end=" ")
                current=current.next