class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sort_array = sorted(nums)  # O(NlogN)
        i = 0
        j = len(sort_array) - 1
        # 從頭尾兩個索引開始來找出相加符合的值
        while i < j:  # O(N)
            total = sort_array[i] + sort_array[j]
            if total < target:
                i += 1
            elif total > target:
                j -= 1
            else:
                num1 = sort_array[i]
                num2 = sort_array[j]
                break
        # 有了值後回去找索引
        idx1 = 0
        idx2 = 0
        for i in range(len(nums)):
            # 如果idx1的值有了就不會進來了
            if nums[i] == num1 and idx1 == 0:
                idx1 = i
            # 如果idx1已經有值就不會再寫成相同的索引了
            if nums[i] == num2 and i != idx1:
                idx2 = i
            if idx1 and idx2:
                break
        return [idx1, idx2]


