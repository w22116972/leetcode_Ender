
## Summary

The negative number is not count for palindrome, so we always return `False`.

## Approach #1 Divide by 10 [Accepted]

**Concept**

We divide x by 10 to get remainder so that we can form the reverse of x.

But we may encounter overflow problem. 

**Algorithm**

1. check whether `x` is negative or `x` is digit in ones
2. let `reverse` be 0 and `remain` be `x`
3. if `remain` is greater than or equal to 10
    1. shift `reverse` left for propagation
    2. cut the right most digit in `remain` to give to `reverse`
    3. shift `remain` right for dropping zero digit
4. compare `reverse` with x which is not including right most digit

**Python**

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x / 10 == 0:
            return True
        remain = x
        reverse = 0
        while remain >= 10:
            reverse *= 10
            reverse += remain % 10
            remain = int(remain / 10)
        return reverse == int(x / 10)
```

**Complexity Analysis**

* Time complexity : $$O(log_10 n)$$.

We divide n by 10 each time, so we have a equation: $$\frac{n}{10^{x}} = 1$$ 

Multiply both sides by $$10^{x}$$

$$n = 10^{x}$$

* Space complexity : $$O(1)$$. 

Only 2 variables for constant memory space.

---

## Approach #2 Comparing in string type [Accpeted]

**Concept**

- To avoid overflow problem, we take the way of converting number to string.
- We convert `x` into string type, so that we can access it with index like `array`.
- But it needs extra memory space for string type of `x`.


**Algorithm**

1. we only need to check half index so we range from 0 to half number of digits.
2. we access it with index, and compare it with the corresponding digits.


**Python**

```python
class Solution(object):
    def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x / 10 == 0:
            return True
        x = str(x)
        n = len(x)
        for i in range(int(n/2)):
            if x[i] != x[n-i-1]:
                return False
        return True
```

**Complexity Analysis**

* Time complexity : $$O(n)$$.

Even we only take half number of digits, the time complexity is O(n/2) = O(n).

* Space complexity : $$O(len(x)) = O(n)$$. 

We need extra memory space for string type of x.

---

## Approach #3 Revert half of digits [Accpeted]

**Concept**

If we have to consider about overflow and no extra constant memory space, we can compare only half number without using string type.
This is also an improved approach #1, we use better `while` loop condition to decrease computing times. 

The key idea is that we mutate `x` and compare it with `reverse`, and we can reach half number of digits when `x <= reverse`.

Note that we need to add a `return` case for even number of digits.
E.g. Asuumed `x = 11`, we exit `while` loop when `x = 1` and `reverse = 1` (`x` is not greater than `reverse`), so we have to ensure `x == reverse`.

**Algorithm**

1. initialize `reverse` to 0
2. we set up `while` condition for `exit when x <= reverse`
3. In `while` loop:
    1. propagate for `reverse`
    2. add right most number in `x` to `reverse`
    3. shift `x` to left for 1 digit
4. return both cases for odd and even number of digits

**Python**

```python
class Solution(object):
    def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = 0
        while x > reverse:
            reverse = reverse * 10
            reverse += x % 10
            x = int(x / 10)
        return x == reverse or x == int(reverse / 10)
```

**Complexity Analysis**

* Time complexity : $$O(n)$$.

We only compare digits for n/2 times, so the time complexity is $$O(n)$$

* Space complexity : $$O(1)$$. 

---