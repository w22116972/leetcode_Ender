class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ele_to_count = {}
        for i in nums:
            if i not in ele_to_count:
                ele_to_count[i] = 1
                if ele_to_count[i] > len(nums) / 2:
                    return i
            elif i in ele_to_count:
                ele_to_count[i] += 1
                if ele_to_count[i] > len(nums) / 2:
                    return i