def missing_num_sumup(nums):
    n = len(nums)
    return n * (n+1) / 2 - sum(nums)


def missing_num_set(nums):
    return (set(range(len(nums) + 1)) - set(nums)).pop()



