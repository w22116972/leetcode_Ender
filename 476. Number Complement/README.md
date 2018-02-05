## Approach #1 Brute Force [Accepted]

**Intuition**

- Use `reverse string` to achieve complement
- Convert `num` to binary format and then to integer format

**Algorithm**

1. convert `num` to binary representation with string type
2. reverse string
3. convert this string to decimal representation with integer type

**Python**

```python
class Solution(object):
    def findComplement(self, num):
        num_bin = ''
        while num > 0:
            if num % 2 == 0:
                num_bin += '1'
            else:
                num_bin += '0'
            num = int(num / 2)

        # python has built-in method to reverse
        num_bin = num_bin[::-1]
        
        # convert binary with string type to decimal with integer type
        num_dec = 0
        for i in range(len(num_bin)):
            num_dec += int(num_bin[i]) * pow(2, (len(num_bin)-1-i))
        return num_dec
```

**Complexity Analysis**

* Time complexity : $$O(n)$$.

- converting string to int takes $$O(len(num_bin)) = O(n)$$
- reversing string needs $$O(len(num_bin)) = O(n)$$ 

* Space complexity : $$O(n)$$.

We need $$O(n)$$ space for storing `num` string type

---
## Approach #2 Bit Manipulation [Accepted]

**Algorithm**



**Python**

```python

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
    