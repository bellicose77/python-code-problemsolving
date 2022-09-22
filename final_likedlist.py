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
    def add_after_node(self,data,x):
        new_node = Node(data)
        if(self.head=='None'):
            print("NOde is empty")
        else:
            n=self.head
            self.x=1
            c=self.x
            while(c!=x):
                n=n.next
                c+=1
            self.temp=n.next
            n.next=new_node
            new_node.next=self.temp
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
    def delete_at_any_position(self,y):
        if self.head == None:
            print("There is nothing")
        else:
            n=self.head
            self.x=1
            c=self.x
            self.p=0
            while c!=y:
                self.p=n
                n=n.next
                c+=1
            self.t=n.next
            self.p.next=self.t

    '''
    def delete_duplicated_node(self):
        n=self.head
        while n.next is not None:
            
            self.x=n.next
            temp=self.x
            #print("temp value before loop",temp.data)
            
            while temp.next is not None:
                #print("is there infite")
                if(n.data==temp.data):
                    n.next=temp.next
                temp=temp.next
            #print("ne=>",n.data)
            else:


                
           
            n=n.next
            '''
    def delete_duplicated_node(self):
        n=self.head
        if n ==None:
            print("Empty linkedlist")
        else:
            while n.next is not None:
                if(n.data==n.next.data):
                    new = n.next.next
                    n.next=new
                else:
                    n=n.next
    def delete_every_duplicate(self):
        n=self.head
        if n==None:
            print("Empty linked")

                
 
#values=[10,20,30,40]   
values=[10,10,10,20,20,30,40,40]    
ll1=LinkedList()
for x in values:
    #ll1.add_begin(x)
    ll1.add_end(x)
#ll1.add_after_node(50,3)
#ll1.delete_at_any_position(3)
#ll1.delete_end()
#ll1.delete_end()
# ll1.delete_begin()
# ll1.delete_begin()
ll1.delete_duplicated_node()
ll1.print_list()
