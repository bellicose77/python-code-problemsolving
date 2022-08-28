node = int(input("Enter number of node: "))
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
while node!=0:
    value = input()
    headnode = Node(value)
    node-=1
    print(headnode.data)