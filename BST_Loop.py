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
    def traverse_node(self,root):
        self.stack =[]
        self.temp=root

    def build_bst(self):
        for x in [7,6,8,3,5]:
            self.insert_node(x)
n1=BST()
n1.build_bst()

