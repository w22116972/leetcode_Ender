class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

test_root = TreeNode(1)
test_root.left = TreeNode(2)
test_root.right = TreeNode(3)
test_root.left.left = TreeNode(4)
test_root.left.right = TreeNode(5) 

def max_depth(root):
    if root is None:
        return 0
    # depth = 1

    # return dfs(root)


def dfs_depth(root, depth):
    if root is None:
        return 0
    if root.val:
        depth += 1
    return max(dfs(root.left, depth), dfs(root.right, depth))

def bfs(root):
    if root is None:
        return 0
    queue = []  # simulate list as queue
    queue.append(root)
    depth = 0
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


def dfs(root):
    if root is None:
        return 0
    go_left = dfs(root.left) 
    go_right = dfs(root.right)
    return max(go_left, go_right) + 1

def dfs_concise(root):
    return max(dfs_concise(root.left), dfs_concise(root.right)) + 1 if root is not None else 0

def maxDepth(root) {
    if root is None:
        return 0
    left_depth = maxDepth(root.left) + 1
    right_depth = maxDepth(root.right) + 1
    return left_depth if left_depth > right_depth else right_depth
}


if __name__ == "__main__":
    print(dfs(test_root))
    # assert max_depth(test_root) == 3