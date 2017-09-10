'''
Find the contiguous subarray within an array 
(containing at least one number) which has the largest sum.

[-2,1,-3,4,-1,2,1,-5,4]
[4,-1,2,1] => 6
'''




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
    At first, we have to check whether given numbers is empty or not
    And if it indeed is an empty list, we return zero

    We set the 2 vars for recording maximal value, local and global
    
    '''
    if len(nums) == 0:
        return 0
    global_max = nums[0]
    local_max = nums[0]
    for n in nums[1:]:
        local_max = max(local_max + n, n)
        global_max = max(local_max, global_max)
    return global_max


def divide_conquer(nums):
    return helper(nums, 0, len(nums)-1)

def helper(nums, left_index, right_index):
    if left_index > right_index:
        return 0
    mid_index = (left_index + right_index) / 2
    left_sum = helper(nums, left_index, mid_index-1)
    right_sum = helper(nums, mid_index+1, right_index)
    left_max_sum, local_sum = 0, 0
    for i in range(mid_index-1, left_index-1, -1):
        local_sum += nums[i]
        left_max_sum = max(local_sum, left_max_sum)
    right_max_sum, local_sum = 0, 0  # clear
    for i in range(mid_index+1, right_index-1, 1):
        local_sum += nums[i]
        right_max_sum = max(local_sum, right_max_sum)
    return max(left_max_sum+nums[mid_index]+right_max_sum, max(left_sum, right_sum))

def brute_force(nums):
    sum_subarray = [[0 for i in range(len(nums))] for j in range(len(nums))]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j < i:
                sum_subarray[i][j] = None
            for k in range(i, j+1):
                sum_subarray[i][j] += nums[k]
    global_max = nums[0]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if sum_subarray[i][j] is not None and sum_subarray[i][j] > global_max:
                global_max = sum_subarray[i][j]
    return global_max

def brute_force_opt(nums):
    global_max = nums[0]
    local_sum = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            local_sum += nums[j]
            if local_sum > global_max:
                global_max = local_sum
        local_sum = 0
    return global_max

assert brute_force([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert brute_force([1]) == 1
assert brute_force([0]) == 0
assert brute_force([-2, -1]) == -1
assert brute_force([-2,1,-3,4,-1,2,1,-5,4]) == 6


assert brute_force_opt([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert brute_force_opt([1]) == 1
assert brute_force_opt([0]) == 0
assert brute_force_opt([-2, -1]) == -1
assert brute_force_opt([-2,1,-3,4,-1,2,1,-5,4]) == 6

# assert maxSubArray([1]) == 1
# assert maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
# assert maxSubArray([0]) == 0
