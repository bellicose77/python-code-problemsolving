class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None
    def insert_node(self,data):
        n=TreeNode(data)
    def print_tree(self):
        pass
n1 = TreeNode(5)
print(n1.data)