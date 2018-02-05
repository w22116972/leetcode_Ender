class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isBalanced_top_down(root):
    '''
    for each node of the tree, 
    get the height of left sub­tree and right sub­tree and check the dif­fer­ence, 
    if it is greater than 1, return false.
    '''
    if root is None:
        return True
    height_difference = abs(get_height(root.left) - get_height(root.right))
    if height_difference > 1:
        return False
    else:
        return isBalanced_top_down(root.left) and isBalanced_top_down(root.right)


def get_height(root):
    if root is None:
        return 0
    else:
        return 1 + max(get_height(root.left), get_height(root.right))


def isBalanced_advanced(root, height=0):
    left_height, right_height = 0, 0
    if root is None:
        height = 0
        return 1
    left_subtree = isBalanced(root.left, left_height)
    right_subtree = isBalanced(root.right, right_height)
    if abs(left_height-right_height) > 1:
        return 0
    else:
        return left_subtree and right_subtree


def isBalanced_bottom_up(root):
    if root is None:  # empty tree
        return True
    return True if recur_bottom_up(root) > 0 else False


def recur_bottom_up(root):
    if root is None:
        return 0
    left_height = recur_bottom_up(root.left)
    if left_height == -1:
        return -1
    right_height = recur_bottom_up(root.right)
    if right_height == -1:
        return -1
    height_difference = abs(left_height - right_height)
    if height_difference > 1:
        return -1
    return 1 + max(left_height, right_height)


def isBalanced_bottom_up_stack(root):
    stack = [root]
    for node in stack:
        if node:
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
    depths = {None: 0}
    for node in reversed(stack):
        if node:
            left_depth = depths[node.left]
            right_depth = depths[node.right]
            if abs(left_depth - right_depth) > 1:
                return False
            depths[node] = 1 + max(left_depth, right_depth)
    return True

