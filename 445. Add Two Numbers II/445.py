class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    l1_int, l2_int = 0, 0
    l1_ptr, l2_ptr = l1, l2
    l1_len, l2_len = 0, 0
    while l1_ptr is not None or l2_ptr is not None:
        if l1_ptr is not None:
            l1_int += l1_ptr.val
            l1_int *= 10
            l1_len += 1
            l1_ptr = l1_ptr.next
        if l2_ptr is not None:
            l2_int += l2_ptr.val
            l2_int *= 10
            l2_len += 1
            l2_ptr = l2_ptr.next
    sum_int = l1_int + l2_int
    sum_int = int(str(sum_int)[::-1])
    dummy_head = ListNode(0)
    dummy_ptr = dummy_head
    while int(sum_int/10) != 0:
        dummy_ptr.next = ListNode(int(sum_int % 10))
        sum_int /= 10
        dummy_ptr = dummy_ptr.next
    dummy_ptr.next = ListNode(int(sum_int % 10))
    return dummy_head.next