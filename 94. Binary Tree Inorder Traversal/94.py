class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorder_traversal_dfs(root):
    traversal = []
    recursion(root, traversal)
    return traversal
    
    
def recursion(node, traversal):
    if node:
        traversal.append(node.val)
        recursion(node.left, traversal)
        recursion(node.right, traversal)


