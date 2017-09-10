#### Approach #1 Recursion [Accepted]

**Intuition**

#### Classify possible cases
Case 1: both nodes are `None`, return `True`
Case 2: one of nodes is `None`, return `False`
Case 3: both values are not equal, return `False`
Case 4: both values are equal, return `True`

#### how to build up recursion call

1. We need 2 recursion calls, one for left subtree, and the other is for right subtree
2. We use `and` to join both calls
    - if at least one call returns `False`, return `False`
    - if both calls return `True`, return `True`
3. ```return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)```

#### Why don't we need case 4 in the code

1. if we return all cases, how can we go further?
2. case 4 end up becoming one of case 1~3 in the end


**Algorithm**

1. We set up return case 1~3
2. We examine subtree recursively.

**Python**

```python
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

**Complexity Analysis**

* Time complexity : $$O(min(p, q))$$.

We won't traverse to additional part, so it only takes minimal number of nodes in `p` and `q`.

* Space complexity : $$O(1)$$.
We don't use any additional memory space.

#### Note: you can also choose case 4 over case 3

```python
if p.val == q.val:
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
return False  # if p.val != q.val
``` 

#### Concise way

```python
def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is not None and q is not None:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
```

---
## Approach #2 Level order traversal using stack  [Accepted]

**Intuition**

We traverse both trees simultaneously and compare the values whenever we `pop` item from stack.

We `append` the pair of identical nodes into stack which is waiting for the next `pop`.

**Algorithm**

1. initialize stack with `p` and `q`
2. if stack has any pairs, we `pop` them and compare them
3. there are 4 cases we need to consider
    1. both nodes are `None`, we proceed to next pair in stack
    2. only one node is `None`, we have to return `False`
    3. values of both nodes are same, we can proceed to consider subtree in both nodes
    4. values of both nodes are different, we have to return `False`
4. after all, if we still didn't return any `False`, it means we have two identical trees.


**Python**

```python
def isSameTree_stack(self, p, q):
        stack = [(p, q)]
        while stack:
            p_node, q_node = stack.pop()
            if p_node is None and q_node is None:
                continue
            elif p_node is None or q_node is None:
                return False
            if p_node.val == q_node.val:
                stack.append((p_node.left, q_node.left))
                stack.append((p_node.right, q_node.right))
            if p_node.val != q_node.val:
                return False
        return True
```

**Complexity Analysis**

* Space complexity : $$O(p U q)$$

- We need stack s for storing pair of `p` and `q`.
- if some node is in `p` instead in `q`, it may cause `stack.append(p.some_node, None)`

So it could be looked like:

`[(p, q), (p, None), (None, q)...]`

So the complexity is union of `p` and `q`

* Time complexity : $$O(p U q)$$

- `list.append()` costs O(1)
- `list.pop()` costs O(1)
- `while stack:` depends on the number of pairs in stack.

so the time complexity is similar to space complexity.


    