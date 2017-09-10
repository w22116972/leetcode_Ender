'''
Find the contiguous subarray within an array 
(containing at least one number) which has the largest product.

[2,3,-2,4]
[2, 3] => 6
'''


def maxProduct(nums):
    '''
    NO extra memory version

    We have to consider the case that the minimum value
    could be the maximun value when the next value is negative.
    So all we need to do is to create a new local_min tracing the negative case.
    '''
    global_max = nums[0]
    pre_min = pre_max = nums[0]
    for n in nums[1:]:
        local_max = max(pre_max * n, pre_min * n, n)
        local_min = min(pre_max * n, pre_min * n, n)
        global_max = max(local_max, global_max)
        pre_max, pre_min = local_max, local_min
    return global_max


def Kadane(nums):
    '''NO pre_max, pre_min Version'''
    if len(nums) == 0:
        return 0
    global_max = local_max = local_min = nums[0]
    for n in nums[1:]:
        # NOTE: Care about data dependency problem, so we use expression: i, j = m, n
        # instead of i = max(i, j, ..); j = min(i, j, ..);
        local_max, local_min = max(local_max * n, local_min * n, n), min(local_max * n, local_min * n, n)
        global_max = max(local_max, global_max)
    return global_max

# assert test([2, 3, -2, 4]) == 6
# assert test([-4, -3, -2]) == 12
# assert test([3, -1, 4]) == 4


def dp(nums):
    local_max = [nums[0]]  
    local_min = [nums[0]]
    global_max = nums[0]
    for i in range(1, len(nums)):
        local_max.append(max(local_max[i - 1] * nums[i], local_min[i - 1] * nums[i], nums[i]))
        local_min.append(min(local_max[i - 1] * nums[i], local_min[i - 1] * nums[i], nums[i]))
        global_max = max(global_max, local_max[i])
    return global_max


def two_loop(nums):
    global_max, local_product = nums[0], 1
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            local_product *= nums[j]
            if local_product > global_max:
                global_max = local_product
        local_product = 1
    return global_max


def dv(nums):
    return recur(nums, 0, len(nums)-1)


def recur(nums, left_index, right_index):
    if left_index > right_index:
        return 1
    mid_index = int((left_index + right_index) / 2)
    # if largest product occurs on the left
    left_subarray_product = recur(nums, left_index, mid_index-1)
    # if largest product occurs on the right
    right_subarray_product = recur(nums, mid_index+1, right_index)
    # if largest product contains mid_index
    # we have to combine left_product, nums[mid_index] and rigt_product
    left_max, local_product = 1, 1
    for i in range(mid_index-1, left_index-1, -1):
        local_product *= nums[i]
        left_max = max(local_product, left_max)
    right_max, local_product = 1, 1
    for i in range(mid_index+1, right_index-1, 1):
        local_product *= nums[i]
        right_max = max(local_product, right_max)
    return max(left_max+nums[mid_index]+right_max, max(left_subarray_product, right_subarray_product))


assert dv([2, 3, -2, 4]) == 6
assert dv([3, -1, 4]) == 4
assert dv([-4, -3, -2]) == 12

assert two_loop([2, 3, -2, 4]) == 6
assert two_loop([3, -1, 4]) == 4
assert two_loop([-4, -3, -2]) == 12

assert dp([2, 3, -2, 4]) == 6
assert dp([3, -1, 4]) == 4
assert dp([-4, -3, -2]) == 12

assert maxProduct([2, 3, -2, 4]) == 6
assert maxProduct([3, -1, 4]) == 4
assert maxProduct([-4, -3, -2]) == 12
