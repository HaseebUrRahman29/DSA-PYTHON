class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
class SinglyLinkedList:
    def __init__(self):
        self.head=None

    def append(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node

    
    def traverse(self):
        if self.head==None:
            print("SLL is empty")
        else:
            curr=self.head
            while curr is not None:
                print(curr.val,end=" ")
                curr=curr.next


    def insert_at(self,val,position):
        new_node=Node(val)
        if position==0:
            new_node.next=self.head
            self.head=new_node
        else:
            current=self.head
            previous=None
            count=0
            while current is not None and count<position:
                previous=current
                current=current.next
                count+=1
            previous.next=new_node
            new_node.next=current


    def delete(self,val):
        curr=self.head
        if curr.next is not None:
            if curr.val==val:
                self.head=curr.next
                del curr
            else:
                found=False
                previous=None
                while curr is not None:
                    if curr.val==val:
                        found=True
                        break
                    previous=curr
                    curr=curr.next
                if found:
                    previous.next=curr.next
                    del curr
                    return
                else:
                    print("Val not found")