node = int(input("Enter number of node: "))
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    def printLinked(self):
        if self.head is None:
            print("Empty linked list")
while node!=0:
    value = input()
    headnode = Node(value)
    node-=1
    print(headnode.data)