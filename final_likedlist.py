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
    def add_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
ll1=LinkedList()
ll1.add_begin(10)