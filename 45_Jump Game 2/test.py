class Solution(object):
    def jump_dp(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        int_max = pow(2, 31) - 1
        min_step = [int_max] * len(nums)
        min_step[0] = 0

        for step in range(1, len(nums)):
            for idx in range(step):
                pass
        for idx in nums:
            for j in range(1, nums[idx]):
                reach_index = j + idx
                if reach_index > len(nums) - 1:
                    break
                if min_step[reach_index] == -1:
                    min_step[reach_index] = 1
                else:
                    min_step[reach_index] = min(min_step[reach_index], step)
            step += 1
        print(min_step)
        print(min_step[-1])

    
    def jump(nums):
        '''
        0.
        last_farthest = 0
        curr_farthest = 0
        step = 0

        1.

        '''
        last_farthest = 0
        curr_farthest = 0
        step = 0
        for i in range(len(nums)):
            if i > last_farthest:
                last_farthest = curr_farthest
                step += 1
            curr_reach = i + nums[i]
            curr_farthest = max(curr_farthest, curr_reach)
        return step


if __name__ == '__main__':
    Solution.jump([2, 3, 1, 1, 4])
# assert Solution.jump([2, 3, 1, 1, 4]) == 2
