# 1. dump all data into one array and sorted this array
# 2. merge sort approach: use 2 pointers to trace

# similar to 23. Merge k Sorted Lists


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def trace_listnodes(l1, l2):
    '''
    tail:
        - to append new nodes easily
        - always points to the last node
    head:
        - to return starting node of this list
        - always points to the first node(init with 0)
    '''
    tail = ListNode(0)
    head = tail
    while l1 is not None or l2 is not None:
        if l1 is None:
            tail.next = l2
            l2 = l2.next
        elif l2 is None:
            tail.next = l1
            l1 = l1.next
        if l1.val > l2.val:
            tail.next = l2
            l2 = l2.next
        else:
            tail.next = l1
            l1 = l1.next
        tail = tail.next
    return head.next  # 初始值0跟此題無關


def recursion(l1, l2):
    node = ListNode(0)
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    if l1.val <= l2.val:
        node = l1
        node.next = recursion(l1.next, l2)
    else:
        node = l2
        node.next = recursion(l1, l2.next)
    return node


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    node = recursion(a, b)
    while node is not None:
        print(node.val)
        node = node.next
