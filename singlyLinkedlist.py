#node = int(input("Enter number of node: "))
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=next
    def printLinked(self):
        if self.head is None:
            print("Empty linked list")
        else :
            n=self.head
            while n is not None:
                print(n.data)
                n=n.next
    def add_begin(self,data):
        new_node = Node(data)
        new_node.next=self.head
        self.head=new_node
ll1 = LinkedList()
ll1.add_begin(10)
ll1.add_begin(20)
ll1.printLinked()

# while node!=0:
#     value = input()
#     headnode = Node(value)
#     node-=1
#     print(headnode.data)