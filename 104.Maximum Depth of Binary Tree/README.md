## Approach #1 DFS by Recursion [Accpeted]

**Intuition**

1. We have to keep go further until we reach the leaves.
2. We need 2 recursive calls for right subtree and left subtree.
3. We use `return` value as depth
    - So each time we go deeper, we `add 1` to return value
    - When we reach the None-node, `return 0` (base case for recursion)
4. different subtree may has different depth, and we use `max` to find longest depth 

**Algorithm**

1. check whether the current node is None
2. make recursive calls and find `max`
3. add 1 to `depth`

**Python**

```python
def dfs(root):
    if root is None:
        return 0
    go_left = dfs(root.left) 
    go_right = dfs(root.right)
    return max(go_left, go_right) + 1
```

```python
def dfs_concise(root):
    return max(dfs_concise(root.left), dfs_concise(root.right)) + 1 if root is not None else 0
```


**Complexity Analysis**

* Time complexity : $$O(n)$$.

DFS will reach every node in tree, so it depends on the number of nodes in tree.

* Space complexity : $$O(1)$$.

We only need constant memory space for value which is returned by recursive calls.

---
## Approach #2 BFS by Queue  [Accepted]

**Intuition**

- We want traverse this tree level by level, so we can add 1 to `depth` between levels.
- We scan nodes in same level, if they have non-None subnode, we put them into `queue`.
- Note that we have to remember how many nodes in this level so that we can aovid to get the node from the next level.

#### note: it is more likely to be level order traversal


**Algorithm**

1. handle root and initialize queue
2. if queue is not empty, we keep looping it
3. we have to remember how many nodes in current level
4. we pick first node in queue to check whether its subnode needs to be put in queue
5. after scaning all nodes in the same level, we can add 1 to `depth`
6. we can proceed to next level if there is node in queue

**Python**

```python
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = []  # simulate list as queue
        queue.append(root)
        depth = 0  # root itself
        while queue:
            node_number_in_level = len(queue)
            for _ in range(node_number_in_level):
                front = queue.pop(0)  # index 0 to pop first element
                if front.left is not None:
                    queue.append(front.left)
                if front.right is not None:
                    queue.append(front.right)
            depth += 1  # we ran through this level
        return depth
```

**Complexity Analysis**

* Time complexity : $$O(n)$$

- `append()`, `len()`, `pop()`: are all $O(1)$.

BFS will walk through all element in array once, although there is `for` looop inside.

* Space complexity : $$O(n)$$
    
We need memory space for queue, which depends on the number of nodes in tree.