class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def print_list(self):
        if self.head==None:
            print("Emptly linked list")
        n=self.head
        while n is not None:
            print(n.data)
            n=n.next
    def add_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
ll1=LinkedList()
ll1.add_begin(5)
ll1.add_begin(10)
ll1.add_begin(15)
ll1.print_list()