## Approach #1 One Stack [Accepted]

**Intuition**

We can use concept of stack to emulate the process of checking valid parenthese.

**Algorithm**

1. we create a list type for `stack`
2. iterate `s`
3. check whether the next character in `s` is left parenthese or not
    - if yes, we append it into `stack`
    - if not, and if it is right parenthese, go to step 4.
    - if not the above case, it is definitely invalid parenthese, so we have to `return False`
4. if the right parenthese is matching the left parenthese which is the last element in stack, we can `pop` the `stack`.
5. after all, if no one left in `stack`, we can said this is valid parenthese.

**Python**

```python
class Solution(object):
    def isValid(self, s):
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            elif c == '}' and len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            elif c == ']' and len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:  # e.g. s = ']'
                return False
        return len(stack) == 0
```

**Complexity Analysis**

* Time complexity : $$O(n)$$.

- Iterating through `s` for time complexity is $$O(len(s)) = O(n)$$.

- `pop`, `append`, `len` of list operations are all $$O(1)$$.

* Space complexity : $$O(n)$$. 

We need $$O(N)$$ space for `stack`.

---
## Approach #2 One stack and One Map [Accepted]

**Intuition**

Use one `map` to avoid multiple `if` conditions.

But it costs extra constant memory space. 

**Algorithm**

1. we have to create mapping for left and right parentheses
2. iterate all character in string
    1. if stack is not empty and if that character is right parenthese
        - we `pop` the stack to see whether two parentheses are match
    2. if that character is left parenthese, all we need to do is `append` it to `stack`.
3. after all, if stack is empty, it means all parenthese `pop` clearly, and we can claim that it is valid parenthese.

**Python**

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        right_to_left = {')':'(',']':'[','}':'{'}
        for c in s:
            if stack and c in right_to_left.keys():  # c is right parenthese
                last_ele = stack.pop()
                if last_ele != right_to_left[c]:
                    return False
                # even if it is equal, we HAVE ALREADY poped it.
            elif c in right_to_left.values():  # c is left parenthese
                stack.append(c)
            else:  # c causes invalid parenthese e.g. s = ']'
                return False
        return stack == []
```

**Complexity Analysis**

* Time complexity : $$O(n)$$. 

- `dict.keys()`, `dict.values()` and `in dict` are all $$O(1)$$.

- Iterating through `s` for time complexity is $$O(len(s)) = O(n)$$.

* Space complexity : $$O(n + 1)) = O(n)$$. 

Although we have an additional dictionary type for mapping parenthese, it only costs constant memory space.