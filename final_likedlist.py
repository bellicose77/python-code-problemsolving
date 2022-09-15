class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def print_list(self):
        if self.head==None:
            print("Emptly linked list")
        n=self.head
        while n is not None:
            print(n.data,"-->",end=" ")
            n=n.next
    def add_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def add_after_node(self,data):
        new_node = Node(data)
    def add_end(self,data):
        new_node = Node(data)
       # print("comming to data",new_node.data)
        if self.head==None:
           # print("coming in if ",new_node.data)
            self.head=new_node
            self.tail=new_node

        else:
            self.tail.next=new_node
            self.tail=new_node

    def delete_end(self):
        
        if self.head==None:
            print("There is no Node")
        else:
            self.temp=None
            n=self.head
            while n.next!=None:
                self.temp=n
                n=n.next
            self.temp.next=None
    
    def delete_begin(self):
        if self.head==None:
            print("There is nothing to delete at first")
        else:
            #print("There are many node to delete")
            n=self.head
            self.head=n.next
    
    def delete_duplicated_node(self):
        n=self.head
        while n.next !=None:
            x=n.next
            if n.data==x.data:
                n.next=x.next
                print(n.data,"--->",x.data)
        n=n.next
                
 
#values=[10,20,30,40]   
values=[1,1,1,2,3,3]    
ll1=LinkedList()
for x in values:
    #ll1.add_begin(x)
    ll1.add_end(x)
#ll1.delete_end()
#ll1.delete_end()
# ll1.delete_begin()
# ll1.delete_begin()
#ll1.delete_duplicated_node()
ll1.print_list()
