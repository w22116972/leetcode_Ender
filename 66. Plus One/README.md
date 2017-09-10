## Approach #1 Very straight way [Accpeted]

**Intuition**

1. get the value of digits and add 1 to it.
2. convert the result into specified return type  

**Algorithm**

1. iterate through `digits` and sum it up.
2. add 1 to `total`
3. convert `total` to string so that we can easily take each digit in `total`
4. put each digit into list and return it


**Python**

```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        total = 0
        for i in range(len(digits)):
            total += digits[i] * pow(10, len(digits) - i - 1)
        total += 1
        total_str = str(total)
        ret_list = []
        for i in total_str:
            ret_list.append(int(i))
        return ret_list
```

**Complexity Analysis**

* Time complexity : $$3 * O(n) = O(n)$$.

- first `for` loop is O(n) because it iterates through `digits` and length of `digits` is `n`
- second `for` loop iterates through `total_str` which length is `n` or `n+1`(if there is propagation)
- `total_str = str(total)` conversion needs O(n)

* Space complexity : $$O(n)$$.

- `total`, `prog` are both O(1)
- `total_str`, `ret_list` are both O(n)

---
## Approach #2 Array Iteration [Accepted]

**Algorithm**

1. starting from least significant digit which is last element in `digits`
2. check whether `carry` bit plus current digit is greater than 9, if yes, set `carry` bit to 1 and calculate current digit after propagation
3. ensure `plus one` only execute once in first place
4. after all, if `carry` is 1, it means there is propagation in the last digit, so we have to put this carry bit in the head of `digits` (the way of doing this may vary from programming languages)

**Python**

```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        i = len(digits) - 1
        plus_one = 1
        while i >= 0:
            if carry + digits[i] + plus_one >= 10:
                digits[i] = carry + digits[i] + plus_one - 10 
                carry = 1
            else:
                digits[i] = carry + digits[i] + plus_one
                carry = 0
            plus_one = 0
            i -= 1
        if carry:
            return [1] + digits
        return digits
```

**Complexity Analysis**

* Time complexity : $$O(n)$$

- `while` is O(n) because `i` is starting from length of digits then minus by 1 every time until `i` reaches 0.  

* Space complexity : $$O(1)$$

`carry`, `i`, `added_one` are all O(1)


#### Note: more concise way

1. We can initialize `carry` to 1 if we want to replace `plus_one`.
2. Use more complicated `for condition` to replace `while`
3. combine `if else` (the way of doing this varies from programming languages)


```python
for i in range(len(digits)-1, -1, -1):
    digits[i] = (digits[i] + carry) % 10
    carry = 1 if digits[i] == 0 and carry == 1 else 0
```

- `carry` can only be 0 or 1
- after adding digit to `carry`, digit is 0 and `carry` is 1 only if digit was 9


```c++
for(int i = digits.size()-1; i >= 0 && carry; i--) {
    carry = (++digits[i]%=10) == 0;
}
```

- In c++ `opertor precedence`, priority of `Prefix increment` (`++d`) is higher than `	Compound assignment by remainder` (`d %= 10`), so it will execute `Prefix increment` first, and then `Compound assignment by remainder`

[cppreference.com](http://en.cppreference.com/w/cpp/language/operator_precedence)

