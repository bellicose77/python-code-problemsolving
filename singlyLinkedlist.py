#node = int(input("Enter number of node: "))
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

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
                print(n.next)
                n=n.next
    def add_begin(self,data):
        new_node = Node(data)
        new_node.next=self.head
        self.head=new_node
    def add_end(self,data):
        new_node = Node(data)
        if self.head==None:
            self.head=new_node
        else:
            while self.head.next==None:
                print("loop e dukhce",self.head.data)
                self.head.next=new_node
                self.head=new_node
                #self.head=new_node


ll1 = LinkedList()
#ll1.add_begin(10)
ll1.add_end(10)
ll1.add_end(20)
ll1.add_end(30)
ll1.add_end(40)
ll1.printLinked()

# while node!=0:
#     value = input()
#     headnode = Node(value)
#     node-=1
#     print(headnode.data)