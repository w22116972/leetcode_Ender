class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_to_ok = {}
        for i in nums:
            if i not in num_to_ok:
                num_to_ok[i] = 1
            else:
                num_to_ok[i] = 2
        return [i for i in num_to_ok.keys() if num_to_ok[i] == 2]