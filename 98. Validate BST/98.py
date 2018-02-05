class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST_inorder(root):
    """
    Property:
    - The left subtree of a node contains only nodes with keys less than the node’s key.
    - The right subtree of a node contains only nodes with keys greater than the node’s key.
    - Both the left and right subtrees must also be binary search trees.
    """
    traversal = []
    inorder_recursion(root, traversal)
    for i in range(1, len(traversal)):
        if traversal[i] < traversal[i-1]:
            return False
    return True
    # print(traversal)


def inorder_recursion(node, traversal):
    if node:
        inorder_recursion(node.left, traversal)
        traversal.append(node.val)
        inorder_recursion(node.right, traversal)

prev = TreeNode(None)
def isValidBST_inorder_cleancode(root):
    '''
    T(n) = n
    S(n) = n for stack space
    '''
    return is_Monotonic_Increasing(root)

def is_Monotonic_Increasing(root):
    if root is None:
        return True
    # recur left subtree
    if is_Monotonic_Increasing(root.left):
        # check wether satisfy definitions
        if prev is not None and root.val <= prev.val:
            return False
        prev = root
        # recur right subtree
        return is_Monotonic_Increasing(root.right)
    return False


def isValidBST_recur(root):
    '''
    T(n) = n^2
    S(n) = n for stack space
    '''
    if root is None:
        return True
    # is_less_than() 只有確認root的val會大於subtree的val，但仍須確認各subtree的val是否也符合，所以還要再傳入isValidBST下去
    return is_less_than(root.left, root.val) and is_greater_than(root.right, root.val) and isValidBST_recur(root.left) and isValidBST_recur(root.right)
 

def is_less_than(node, val):
    if node is None:
        return True
    return node.val < val and is_less_than(node.left, val) and is_less_than(node.right, val)


def is_greater_than(node, val):
    if node is None:
        return True
    return node.val > val and is_greater_than(node.left, val) and is_greater_than(node.right, val)

def isValidBST_top_down(root):
    '''
    T(n) = n
    S(n) = n for stack space
    '''
    max_int = pow(2, 63) - 1
    min_int = -pow(2, 63)
    return top_down_recursion(root, min_int, max_int)

def top_down_recursion(root, low, high):
    if root is None:
        return True
    return low < root.val and high > root.val and top_down_recursion(root.left, low, root.val) and top_down_recursion(root.right, root.val, high)

def isValidBST_top_down_None_version(self, root):
    '''
    Previous solution may fail when there is maximal value or minimal value in this tree
    So we use None to represent extreme value
    '''
    return self.top_down_recursion(root, None, None)

def top_down_recursion_None_version(self, root, low, high):
    if root is None:
        return True
    return (low is None or low < root.val) and (high is None or high > root.val) and self.top_down_recursion(root.left, low, root.val) and self.top_down_recursion(root.right, root.val, high)



root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

isValidBST(root)