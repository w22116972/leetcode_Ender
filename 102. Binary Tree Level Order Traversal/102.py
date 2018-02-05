class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(None)
n5 = TreeNode(None)
n6 = TreeNode(15)
n7 = TreeNode(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

# [Accepted]
def level_order_queue(root):
    if root is None:
        return []
    node_queue = [root]  # simulate list as node_queue
    level_order = []
    while node_queue:
        node_count_on_level = len(node_queue)
        node_on_level = []
        for _ in range(node_count_on_level):
            front = node_queue.pop(0)  # index 0 to pop first element
            if front.val is not None:
                node_on_level.append(front.val)
                if front.left:
                    node_queue.append(front.left)
                if front.right:
                    node_queue.append(front.right)
        level_order.append(node_on_level)
    return level_order

print(level_order_queue(n1))

