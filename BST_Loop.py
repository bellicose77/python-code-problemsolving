class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert_node(self,data):
        if self.root is None:
            self.root = TreeNode(data)
            return
        temp=self.root
        while True:
            if temp.data > data:
                if temp.left:
                    temp=temp.left
                else:
                    temp.left=TreeNode(data)
                    break
            else:
                if temp.right:
                    temp=temp.right
                else:
                    temp.right=TreeNode(data)
                    break
    def in_order(self,root):
        print("Inorder")
        self.stack =[]
        temp=self.root
        while self.stack or temp:
            while temp:
                self.stack.append(temp)
                temp = temp.left
            k=self.stack.pop()
            print(k.data)
            k=temp.right

    def build_bst(self):
        for x in [7,6,8,3,5]:
            self.insert_node(x)
        #self.in_order(7)
n1=BST()
n1.build_bst()
n1.in_order(7)
n1.in_order(6)

