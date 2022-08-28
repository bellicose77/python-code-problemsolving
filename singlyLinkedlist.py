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
        else :
            n=self.head
            while n is not None:
                print(n.data)
 
                n=n.next
ll1 = LinkedList()
ll1.printLinked()
# while node!=0:
#     value = input()
#     headnode = Node(value)
#     node-=1
#     print(headnode.data)