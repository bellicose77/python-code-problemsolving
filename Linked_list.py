class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
#first = Node(3)
ll = LinkedList()
ll.head=Node(3)
print(ll.data)
print(ll.next)
