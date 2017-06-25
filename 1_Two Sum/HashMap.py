class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}  # dictionary {} 在python有key-value的用途
        for i in range(len(nums)):
            x = nums[i]
            if target - x in hashmap:  # 如果target - x 是hashmap的key
                return [hashmap[target - x], i]  # [符合target- x 的value, x的索引]
            hashmap[x] = i  # 沒找到的話就把陣列值當成key，陣列索引當成value