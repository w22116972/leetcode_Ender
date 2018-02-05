class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global_max = 0
        local_max = 0
        for i in nums:
            if i == 1:
                local_max += 1
            elif i == 0:
                if local_max > global_max:
                    global_max = local_max
                local_max = 0
        if local_max > global_max:
            global_max = local_max
        return global_max