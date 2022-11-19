class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None

    def insert_node(self,data):
        if self.root is None:
            self.root = TreeNode(data)
            return 
        current_node=self.root
        #print(current_node.data)
        previous_node = None
        #print(previous_node)
        while current_node:
            previous_node=current_node
            print("previous_node",previous_node)
            if data < current_node.data:
                current_node=current_node.left
                #print("prevous node value in if",current_node,previous_node,data)
            else :
                current_node=current_node.right
                #print("prevous node in if",current_node,previous_node,data)
        if data <previous_node.data:
            print("previous node data ",previous_node.data)
            previous_node.left=TreeNode(data)
        else:
            previous_node.right = TreeNode(data)
        

    def print_tree(self):
        pass
    def build_tree(self):
        for x in [7, 6, 8, 5]:
            self.insert_node(x)
n1 = Tree()
n1.build_tree()