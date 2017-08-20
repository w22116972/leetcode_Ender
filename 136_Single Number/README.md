


## Approach #1 List operation [Time Limit Exceeded]

**Algorithm**

1. declare array of list type
2. check all the elements in `nums`
3. if some number in `nums` is new to array, append it
4. if some number is already in array, remove it


**Python**

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()
```

**Complexity Analysis**

* Time complexity : $$O(n^2)$$.

1. we iterate through `nums`, so the time complexity is $$O(n)$$
2. We search the whole list to find whether there is duplicate number, so the time complexity is $$O(n)$$
3. Because search is in the `for` loop, so we have to multiply both time complexities which is $$O(n * n)$$.

* Space complexity : $$O(n)$$. 

We need `list` to contain elements in `nums`.

---
## Approach #2 Hash Table [Accepted]

**Algorithm**

We use hash table to avoid $$O(n)$$ for searching elements.

1. iterate through all elements in `nums`
2. try if `hash_table` has the key for `pop`
3. if not, set up key/value pair
4. in the end, there is only one element in `hash_table`, so use `popitem` to get it

**Python**

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]
```

**Complexity Analysis**

* Time complexity : $$O(n * 1) = O(n)$$. 

1. Time complexity of `for` loop is $$O(n)$$
2. Time complexity of hash table(dictionary in python) operation `pop` is $$O(1)$$

* Space complexity : $$O(n)$$.

`hash_table` needs space for number of elements in `nums`.

---
## Approach #3 Math [Accepted]

**Concept**

2 * (a + b + c) - (a + a + b + b + c) = c

**Python**

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)
```

**Complexity Analysis**

* Time complexity : $$O(n + n) = O(n)$$. 

`sum` will call `next` to iterate through `nums`.
We can see it as `sum(list(i for i in nums))` which means the time complexity is `O(n)` because of the number of elements in `nums`.

* Space complexity : $$O(n + n) = O(n)$$.

`set` needs space for the number of elements in `nums`

---
## Approach #4 Bit Manipulation [Accepted]

**Concept**

- if XOR zero and some bit, it will return that bit
- if XOR two same bits, it will return 0

- a ^ 0 = a
- a ^ a = 0
- a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b

So we can XOR all together to find the unique number.

**Python**

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
```

**Complexity Analysis**

* Time complexity : $$O(n)$$. 

We only iterate through `nums`, so the time complexity is the number of elements in `nums`.

* Space complexity : $$O(1)$$.

