class Solution(object):
    def searchInsert(self, nums, target):
        """
        T = O(n)
        S = O(1)
        """
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)