class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorderTraversal_recur(root):
    traversal = []
    recursion(root, traversal)
    return traversal


def recursion(node, traversal):
    if node:
        traversal.append(node.val)
        recursion(node.left, traversal)
        recursion(node.right, traversal)


def preorderTraversal_dfs(root):
    stack = [root]
    traversal = []
    while len(stack) > 0:
        current_node = stack.pop()
        if current_node:
            traversal.append(current_node.val)
            stack.append(current_node.right)  # 之後left要先被pop出來，所以要比right晚被push進去
            stack.append(current_node.left)
    return traversal


def morris_traversal(root):
    traversal = []
    while root is not None:
        if root.left is None:
            traversal.append(root.val)
            root = root.right
        else:
            next_node = root.left
            while next_node.right is not None and next_node != root:
                next_node = next_node.right
            if next_node.right is None:
                next_node.right = root
                traversal.append(root.val)
                root = root.left
            else:
                next_node.right = None
                root = root.right
    return traversal
