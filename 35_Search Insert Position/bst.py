def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    assert(searchInsert([1, 3, 5, 6], 5) == 2)
    assert(searchInsert([1, 3, 5, 6], 7) == 4)
    assert(searchInsert([1, 3, 5, 6], 0) == 0)
