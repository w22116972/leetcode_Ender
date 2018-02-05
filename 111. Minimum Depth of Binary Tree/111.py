class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def minDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    if root.left is None:
        return 1 + minDepth(root.right)
    if root.right is None:
        return 1 + minDepth(root.left)
    return 1 + min(minDepth(root.left), minDepth(root.right))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)


print(minDepth(root))