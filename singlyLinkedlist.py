class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

headnode = Node(3)
print(headnode.next)