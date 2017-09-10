## Approach #1  [Time Limit Exceeded]

**Intuition**

- Outer `for` is used for indexing of beginning of subarray
- Inner `for` helps `local_product` multiply number from beginning to the end, and if greater product exists, we have to update `global_max`
- initial value of `local_product` must be `1` because it is prodcut not adding


**Algorithm**

1. initialize variables 
2. iterate two `for` loop 
    - range of inner `for` is from `i` to end of `nums`
3. calculate `local_product`
4. update `global_max`
5. clear `local_product` to 1

**Python**

```python
class Solution(object):
    def maxProduct(self, nums):
        global_max, local_product = nums[0], 1
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                local_product *= nums[j]
                if local_product > global_max:
                    global_max = local_product
            local_product = 1
        return global_max
```

**Complexity Analysis**

* Time complexity : $$O(n^{2})$$

- Outer `for` loop is $$O(len(nums)) = O(n)$$
- Inner `for` liip is $$O(len(nums)-i) = O(n)$$


* Space complexity : $$O(1)$$

- `global_max`, `local_product` are all O(1)

---

## Approach #2 Dynamic Programming with Array  [Accepted]

**Note**

- negative number may become the largest product when being multiplied by a negative number
    - so we have to keep track of previous negative number
- one of three cases may becomes largest prodcut:
    1. previous maximum multiplied by current value (both are positive)
    2. previous minimum multiplied by current value (both are negative)
    3. current value 
> max(local_max[i - 1] * nums[i], local_min[i - 1] * nums[i], nums[i]))

**Algorithm**

1. initialize `local_max` and `local_min` to the array containing the first number
2. iterate through `nums`
3. use `precede local value` in `local_max/min` to find current max and min
4. append current max and min to `local_max` and `local_min`
5. update `global_max`

**Python**

```python
class Solution(object):
    def maxProduct(self, nums):
        local_max = [nums[0]]
        local_min = [nums[0]]
        global_max = nums[0]
        for i in range(1, len(nums)):
            local_max.append(max(local_max[i - 1] * nums[i], local_min[i - 1] * nums[i], nums[i]))
            local_min.append(min(local_max[i - 1] * nums[i], local_min[i - 1] * nums[i], nums[i]))
            global_max = max(global_max, local_max[i])
        return global_max
```

**Complexity Analysis**

* Time complexity : $$O(n)$$

- range of `for` is from 1 to `len(nums)`, so it is $$O(n)$$
- `append element to end of list` is O(1)

* Space complexity : $$O(n)$$

- `local_max` and `local_min` are $$O(n)$$ because they keep appending number until they reach the end of `nums` 
    
---

## Approach #3 Dynamic Programming without Array [Accpeted]

**Algorithm**

1. initialize variables
2. iterate through array 
3. calculate local value (considering 3 cases)
4. update `global_max`

**Python**

```python
class Solution(object):
    def maxProduct(self, nums):
        global_max = nums[0]
        local_min = nums[0]
        local_max = nums[0]
        for n in nums[1:]:
            local_max = max(local_max * n, local_min * n, n)
            local_min = min(local_max * n, local_min * n, n)
            global_max = max(local_max, global_max)
        return global_max
```

**Complexity Analysis**

* Time complexity : $$O(n)$$.

`for` loop iterates $$n-1$$ times, which is $$O(n)$$

* Space complexity : $$O(1)$$.

- `global_max`, `pre_min`, `pre_max` are all $$O(1)$$

---

## Approach #4 Divide and Conquer  [Accpeted]

**Intuition**

- 

**Algorithm**

1. initialize variables
2. iterate through array 
3. calculate local value (considering 3 cases)
4. update `global_max`

**Python**

```python
class Solution(object):
    def maxProduct(self, nums):
        global_max = nums[0]
        local_min = nums[0]
        local_max = nums[0]
        for n in nums[1:]:
            local_max = max(local_max * n, local_min * n, n)
            local_min = min(local_max * n, local_min * n, n)
            global_max = max(local_max, global_max)
        return global_max
```

**Complexity Analysis**

* Time complexity : $$O(n)$$.

`for` loop iterates $$n-1$$ times, which is $$O(n)$$

* Space complexity : $$O(1)$$.

- `global_max`, `pre_min`, `pre_max` are all $$O(1)$$
