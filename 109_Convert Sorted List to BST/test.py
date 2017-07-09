class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        tree = TreeNode(head.val)
        while head:
            self.dfs(head.next, tree)

    def dfs(head, tree):
        if head is None:
            return
        elif head.val > tree.val and tree.right is None:
            tree.right.val = head.val
            return 
        elif head.val > tree.val and tree.right is not None:
            self.dfs(head, tree.right)
        elif head.val <= tree.val and tree.left is None:
            tree.left.val = head.val
            return
        elif head.val <= tree.val and tree.left is not None:
            self.dfs(head, tree.left)
