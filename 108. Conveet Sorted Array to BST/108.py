class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        T = O(n)
        S = O(log n)

        We use divide and conquer technique to solve this problem.
        1. pick middle element in sorted array as root in each interation.
        2. now we have to subarray which can be seen as left subtree and right subtree.

        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.divide_conquer(nums, 0, len(nums) - 1)

    def divide_conquer(self, arr, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        node = TreeNode(arr[mid])
        node.left = self.divide_conquer(arr, start, mid - 1)
        node.right = self.divide_conquer(arr, mid + 1, end)
        return node
