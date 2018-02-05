def findContentChildren(g, s):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """
    greed = sorted(g)
    size = sorted(s)
    greed_index = 0
    size_index = 0
    count = 0
    while greed_index != len(g) and size_index != len(s):
        if greed[greed_index] == size[size_index]:
            count += 1
            greed_index += 1
            size_index += 1
        elif greed[greed_index] > size[size_index]:
            size_index += 1
        else:
            greed_index += 1
    return count


def findContentChildren_sort(g, s):
    g.sort()
    s.sort()
    count = 0
    greed_index = 0
    for cookie in s:
        if greed_index >= len(g):
            break
        if cookie >= g[greed_index]:
            count += 1
            greed_index += 1
    return count

def findContentChildren_sort2(self, g, s):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """
    g, s = sorted(g), sorted(s)
    i, j= 0, 0
    while i != len(g) and j != len(s):
        if s[j] >= g[i]:
            i = i+1
        j += 1
    
    return i


def hash_table(g, s):
    greed = {}
    size = {}


class Node:
    def __init__(self, val):
        self.left_child = None
        self.right_child = None
        self.data = val


def insert_bst(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left_child is None:
                root.left_child = node
            else:
                bst_insert(root.left_child, node)
        else:
            if root.right_child is None:
                root.right_child = node
            else:
                bst_insert(root.right_child, node)


def findContentChildren_bst(g, s):
    root = None
    for i in range(s):
        insert_bst(root, s[i])
        

def test(f):
    assert f([1,2,3], [1,1]) == 1
    assert f([1,2,3], [1,1]) == 1


test(findContentChildren)
