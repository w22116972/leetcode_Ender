def maxSubArray(nums):
    '''
    1. dp[i]: 紀錄從頭到index i時，最大的sum
    - 如果加了目前index i的值能夠變大，就取最大的
    2. max_sum: 紀錄目前最大的sum值
    '''
    if len(nums) == 0:
        return 0
    dp = [nums[0]]
    max_sum = nums[0]
    for i in range(1, len(nums)):
        dp.append(max(dp[i - 1] + nums[i], nums[i]))
        max_sum = max(max_sum, dp[i])
    return max_sum


def Kadane(nums):
    '''
    '''
    global_max = local_sum = nums[0]
    for n in nums[1:]:
        global_max = max(global_max + n, n)
        local_sum = max(local_sum, global_max)
    return local_sum


assert maxSubArray([1]) == 1
assert maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert maxSubArray([0]) == 0
