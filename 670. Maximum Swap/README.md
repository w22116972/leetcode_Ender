
## Summary: Greedy Algorithm

We want to get the largest number, so if there is a less significant digit larger than the most significant digit, we have to swap them.

If the most significant bit is already 9 which is largest, we check the next most significant bit.

#### Although the given number is at most 8-bits, I still consider it as n-bits. 


## Approach #1 Brute Force with String approach [Accepted]

**Brute Force Intuition**

iterate digit from most significant to least significant, and swap it with lower digit to check whether result becomes bigger after swapping. 

**String approach Intuition**

The easy way to swap digits is to use array accessing, but digits can't be converted to array directly.

Here we convert digits to string first, so when it is converted to array later, each digit is stored exactly in each element in array

**Algorithm**

1. convert `num` into list type in Python (like `array` in others)
    - in order to swap digits easily
    - because `string` can't be reassigned in Python
2. copy `num` to `num_max`
3. start `for` loop from most significant bit to least significant bit in `nums`
4. second `for` loop finds whether other bit is good for exchanging
5. (optional) check whether digit is greater than current digit
    - if it is not greater, then obviously it is impossible that swapped value becomes greater 
6. swap digit
7. convert list to integer type, so we can compare which is bigger
8. swap back
9. after all, return `num_max`

**Python**

```python
class Solution(object):
    def maximumSwap(self, num):
        num_list = list(str(num))
        num_max = num_list[:]
        for current_index in range(len(num_list)):
            for swap_index in range(current_index+1, len(num_list)):
                if int(num_list[swap_index]) > int(num_list[current_index]):
                    num_list[swap_index], num_list[current_index] = num_list[current_index], num_list[swap_index]
                    if int(''.join(num_list)) > int(''.join(num_max)):
                        num_max = num_list[:]
                    num_list[swap_index], num_list[current_index] = num_list[current_index], num_list[swap_index]
        return int(''.join(num_max))
```

`''.join(num_list)` is a way of convert list to string in Python

**Complexity Analysis**

* Time complexity : $$O(n^{3})$$.

- `list(str(num))` is $$O(2 * n), because converting integer to string is $$O(n)$$ and converting string into list is also $$O(n)
- `num_max = num_list[:]` is $$O(n)$$ because it copies a whole list
- Outer `for` loop is $$O(n)$$ because it iterates through whole list
- Inner `for` loop is $$O(n)$$ because $$O(n - i) = O(n)$$
- `''.join(num_max)` is $$O(n)$$ because it joins all numbers in list

The latter three complexities are nested, so they have to multiply together.

Overall time complexity is $$O(n) * O(n) * O(n) = O(n^{3})$$

* Space complexity : $$O(n)$$.

- `num_max = num_list[:]` needs $$O(n)$$ memory space
- `''.join(num_max)` is $$O(n)$$ 

---
## Approach #2 Brute Force with Integer approach  [Accepted]

**Integer approach Intuition**

Use integer division to create a array consisting of digits

scan `num` from 
- `max_digit_from_least`, `max_index_from_least`, `current_index` store temporal value during iteration
- `swap_index 1,2` stores global 

**Algorithm**

1. 
2. 

**Python**

```python
class Solution(object):
    def maximumSwap(self, num):
        max_digit_from_least = 0
        max_index_from_least = -1
        current_index = 0
        swap_index1 = 0
        swap_index2 = 0
        num_from_least = []
        while num > 0:
            digit = num % 10
            num_from_least.append(digit)
            if max_digit_from_least > digit:
                swap_index1 = current_index
                swap_index2 = max_index_from_least
            elif digit > max_digit_from_least:
                max_digit_from_least = digit
                max_index_from_least = current_index
            num = int(num / 10)
            current_index += 1
        num_from_least[swap_index1], num_from_least[swap_index2] = num_from_least[swap_index2], num_from_least[swap_index1]
        total = 0
        for i in range(len(num_from_least)):
            total += (int)(num_from_least[i] * 10**i)
        return total
```

**Complexity Analysis**

* Time complexity : $$O()$$

* Space complexity : $$O()$$
    
---
## Approach #3  [Accepted]

**Algorithm**



**Python**

```python

```

**Complexity Analysis**

* Time complexity : $$O()$$

* Space complexity : $$O()$$
    

---
## Approach #4 Dynamic Programming  [Accepted]

**Concept**

因為要交換出最大值，從greedy的角度來看，先把最高位數換成最大值，如果最大位數已經是該數列最大了，再從第二大位數開始

求出從最低位數開始的`目前最大值的索引`

假設從最高位數開始,
- 如果目前的索引和dp的索引不同，代表其他地方有更大的值
- 如果目前的索引和dp的索引相同，代表右邊已經沒有其他更大的值



Start from least significant bit, 

**Example** 

dp[key] = value
- key = index of `num`
- value = index of largest number starting from right(least significant bit)

e.g. given 2736

start from least significant bit, and 6 is maximal digit so far, so we store its index to dp i.e. dp[3] = 3(index of 6).

now, 273

3 is not the maximal digit, so dp[2] = 3 (still index of 6)

then, 27

7 is greater than 6, so dp[1] = 1(index of 7)

finally, 2

2 is less than 7, so dp[0] = 1(still index of 7)

so dp = [1, 1, 3, 3]

and we start from most significant bit because 從最前面的swap才會有最大的值

dp[0] = 1 != num[0] = 2

so we swap them to get maximum value


**Algorithm**

1. convert `num` to list type so that we can easily manipulate digit in `num`
2. construct `dp` with initial value 1
3. start from least significant bit to most significant bit, and we check whether exist greater digit
4. we store index of current maximal value in `dp`
5. start new loop from most significant bit, 


**Python**

```python
class Solution(object):
    def maximumSwap(self, num):
        num_str = list(str(num))
        dp = [-1]*len(num_str)
        current_max_index_from_least = len(num_str)-1
        for i in range(len(num_str)-1, -1, -1):
            if num_str[i] > num_str[current_max_index_from_least]:
                current_max_index_from_least = i
            dp[i] = current_max_index_from_least
        for i in range(len(num_str)-1):
            if num_str[dp[i]] != num_str[i]:
                num_str[i], num_str[dp[i]] = num_str[dp[i]], num_str[i]
                break
        return int(''.join(num_str))
```

**Complexity Analysis**

* Time complexity : $$O(n)$$

- convert `num` to string and to list type: $$O(n+n)$$
- range of first `for` loop is length of `num`: $$O(n)$$
- range of second `for` loop is length of `num`: $$O(n)$$
- `int(''.join(num_str))`: $$O(n)$$


* Space complexity : $$O(n)$$

- size of `dp` is length of `num`, which is $$O(n)$$