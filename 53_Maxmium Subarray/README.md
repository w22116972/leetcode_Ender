
## Approach # 1 Brute Force with Array [Time Limit Exceeded]

**Intuition**

- Use 2-dimension array `sum_subarray` to record maximial sum at index i to j
- We need 3 `for` loops, two of them are for index i and j, the another one is  used for `accumulate values between i and j`
- Tricky part is how to set up initial value
    - if we set initial value to 0 and `nums` has all negative values, then initalize value may become `global_max`
    - because `j < i` causes us to not update with initial value
    - so you can adjust loop condition or make a `if` condition to solve it
    - here I choose to make a new `if` condition
- Usage of `global_max = nums[0]` is equal to `global_max = INT_MIN` here

**Algorithm**

1. initialize `sum_subarray` to 2 dimension array
2. use 3 `for` loops to record maximal sum to `sum_subarray`
3. iterate through entire `sum_subarray` to find `global_max` 

**Python**

```python
class Solution(object):
    def maxSubArray(self, nums):
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
```

**Complexity Analysis**

* Time complexity : $$O(n^{3})$$.

- 2 `for` loop with length of `nums` and 1 inner loop with at most length n, so the time complexity is $$O(n) * O(n) * O(n)$$

* Space complexity : $$O(n^{2})$$.

- `global_max` is $$O(1)$$
- `sum_subarray` is two-dimension array and size of each dimensino is $$O(n)$$, so the space complexity is $$O(n^{2})$$

---

## Approach # 2 Brute Force without Array [Time Limit Exceeded]

**Intuition**

1. improve `for` condition
    - Outer: index of beginning of subarray
    - Inner: index of beginning to the end, we check whether greater sum exists in every iteration.
2. we only need sum of subarray, so we can simply use `local_sum` instead of array `sum_subarray`

**Algorithm**

1. Outer `for` is used for indexing beginning of subarray
2. Inner `for` is used for looping through `begin` to `end`
3. update `global_max`
4. clear `local_sum`


**Python**
```python
class Solution(object):
    def maxSubArray(self, nums):
        global_max = nums[0]
        local_sum = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                local_sum += nums[j]
                if local_sum > global_max:
                    global_max = local_sum
            local_sum = 0
        return global_max
```
**Complexity Analysis**

* Time complexity : $$O(n^{2})$$.

- Outer loop is $$O(n)$$
- Inner loop is $$O(n-i) = O(n)$$

* Space complexity : $$O(1)$$.

- `global_max`, `local_sum` are both $$O(1)$$

---

## Approach # 3 Dynamic Programming [Accpeted]

**Intuition**

- define: `dp[i]` is maximum sum of subarray ending at index i
- choose maximum of 2 cases: 
    1. adding current value to current sum of subarray is greater
    2. current value is greater than current sum of subarray
- Dynamic programming formula: `dp[i] = max(dp[i-1] + nums[i], nums[i])`
    - `dp[i]` here is *result at index i*; however, maybe there is another greater sum at index j, which is why we have to use `global_max` to record maximum sum of subarray at any index before i.


**Algorithm**

1. initialize `local_max`, `global_max`
2. iterate through array 
3. apply formula to `local_max`
4. update `global_max`


**Python**

```python
class Solution(object):
    def maxSubArray(self, nums):
        local_max = nums[0]
        global_max = nums[0]
        for i in range(1, len(nums)):
            local_max = max(local_max + nums[i], nums[i])
            global_max = max(global_max, local_max)
        return global_max
```

**Complexity Analysis**

* Time complexity : $$O(n)$$.

- `for` loop iterates `n-1` times, so it takes $$O(n-1) = O(n)$$

- `max` is $$O(1)$$

* Space complexity : $$O(1)$$.

- `local_max`, `global_max` are both O(1)

---
## Approach # 4 Divide and Conquer  [Accepted]

**Concept**

We can divide `nums` at `mid_index` and each subarray has 2 possible situations that may have largest sum.


#### Case 1: Contain value at `mid_index`

    - left_subarray_sum + nums[mid_index] + right_subarray_sum
    - here we can use *recursion* to find `left_subarray_sum` and `right_subarray_sum`

#### Case 2: Not contain value at `mid_index`
    - if largest sum is on left, return `left_sum`
    - if largest sum is on right, return `right_sum`



**Algorithm**

1. Define recursion function with arguments in `left_index`, `right_index` so that we can easily divide array to do recursion
2. In recursion function, we define `mid_index` with middle of `left_index` and `right_index`
3. Handle case 1 with two recursion functions
4. Handle case 2 by calculating `left_sum` and `right_sum` in current partition range 

**Python**

```python
def divide_conquer(nums):
    return helper(nums, 0, len(nums)-1)

def helper(nums, left_index, right_index):
    if left_index > right_index:
        return 0
    mid_index = (left_index + right_index) / 2
    # case 1: no containing value at `mid_index`
    left_subarray_sum = helper(nums, left_index, mid_index-1)
    right_subarray_sum = helper(nums, mid_index+1, right_index)
    # case 2: containing value at `mid_index`
    left_max_sum, local_sum = 0, 0
    for i in range(mid_index-1, left_index-1, -1):
        local_sum += nums[i]
        left_sum = max(local_sum, left_max_sum)
    right_max_sum, local_sum = 0, 0  # clear
    for i in range(mid_index+1, right_index-1, 1):
        local_sum += nums[i]
        right_sum = max(local_sum, right_max_sum)
    
    return max(left_sum+nums[mid_index]+right_sum, max(left_subarray_sum, right_subarray_sum))  # maximium of 3 cases

```

**Complexity Analysis**

* Time complexity : $$O(n log n)$$

- Divide array into two `n/2` size array: $$T(n) = 2T(\frac{n}{2})$$
- Calculate `left_sum` and `right_sum` are both $$O(n)$$
- So the formula is $$T(n) = 2T(\frac{n}{2}) + O(n)$$

* Space complexity : $$O(log n)$$

1. Although each variable is $$O(1)$$, in recusrion procedure we may occupy stack space
2. We see these elements as a single `decision tree`, so when we divide it into half each time, the height of decision tree is $$log_2 n$$, which means we need to calculate $$log_2 n$$ times in worst case
3. i.e. In stack space, the number of each kind of variable is up to $$log_2 n$$
4. `left_subarray_sum` and `right_subarray_sum` are both occupy $$log_2 n$$ in stack space
5. so the space complexity is $$2 * O(log_2 n) = O(log n)$$


---
