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
    def in_order(self):
        self.stack =[]
        self.temp=self.root
        while self.stack or temp:
            while temp:
                self.stack.append(temp)
                temp = temp.right
            k=self.stack.pop()
            print(k.value)
            k=temp.right

    def build_bst(self):
        for x in [7,6,8,3,5]:
            self.insert_node(x)
        self.in_order()
n1=BST()
n1.build_bst()

