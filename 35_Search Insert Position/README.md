# Summary

If some value is greater or equal to the target value, the position of that value is where we want to insert into.
If target value is greater than all values in `nums`, we have to return the index which is greater than maximal index in `nums`.

# Solution

## Approach #1 Linear Search [Accepted]

**Algorithm**

1. iterate array with index
2. return index if any value is greater or equal to the target value
3. return length of array if target is greater than all values in `nums`

**Python**

```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
```

**Complexity Analysis**

* Time complexity : $$O(n)$$.

The `for loop` is starting from 0 to length of given array.

So the time complexity is `n` 

* Space complexity : $$O(1)$$. We didn't use any additoinal data structure.

---

## Approach #2 Binary Search [Accepted]

**Intuition**

Given sorted array to find something, we can use binary search.

**Algorithm**

1. pick middle of array for pivot
2. if that pivot is smaller than target, keep finding in the left half of array
3. or if pivot is greater than target, keep finding in the right half of array
4. when `while loop` ends, `right` <= `target` <= `left`
5. return `left` because 
> If some value is greater or equal to the target value, the position of that value is where we want to insert into.

**Python**

```python
class Solution(object):
    def searchInsert(self, nums, target):
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
```

**Complexity Analysis**

* Time complexity : $$O(log_2 n) = O(log n)$$. 

First proof:

The worst case is reached when binary search has reduced to one element.

So we have to calculate how many times we divide n by 2 until we have 1.

Let us denote T(n) as the number of checks and T(1) = 1.

We compute the middle of range, so `T(n/2)`

And we only check one number each time, so `+ 1`

Finally, we have recurrence: `T(n) = T(n/2) + 1`

e.g. T(n) = T(n/2) + 1 = T(n/4) + 1 + 1 ... = T(1) + ? * 1

$$ \frac{n}{2^{x}} = 1 $$

we multiply it by $$2^{x}$$

$$ 2^{x} = n $$

we `log` it

$$ x = log_2 n $$

* Space complexity : $$O(1)$$. We only need 3 variables for memory space.
    