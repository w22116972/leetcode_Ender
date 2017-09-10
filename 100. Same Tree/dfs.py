class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

test_root = TreeNode(1)
test_root.left = TreeNode(2)
test_root.right = TreeNode(3)
test_root.left.left = TreeNode(4)
test_root.left.right = TreeNode(5) 

p = test_root
q = test_root
r = test_root.right.right = TreeNode(6)

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree_stack(self, p, q):
        stack = [(p, q)]
        while stack:
            p_node, q_node = stack.pop()
            if p_node is None and q_node is None:
                continue
            elif p_node is None or q_node is None:
                return False
            if p_node.val == q_node.val:
                stack.append((p_node.left, q_node.left))
                stack.append((p_node.right, q_node.right))
            if p_node.val != q_node.val:
                return False
        return True