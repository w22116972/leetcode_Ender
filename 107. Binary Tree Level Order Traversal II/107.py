# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
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
        return level_order[::-1]
            
        