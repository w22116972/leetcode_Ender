def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    
    The simple solution is to add up both values of node and check whether there is carry value. 
    Then trace down the list node with carry value.
    
    We calculate the first node in L1 and L2.
    Before we traverse the entire list node, 
    note that when you trace down list node and end up calculation, you won't get first node for answer easily. 
    So we have to save the first node for answer. 

    The condition of while loop is one of the list node having the next node or carry bit equaling to one
    But what if one of the list node is shorter than the other or the next node of both L1 and L2 is None while carry node is equal to one
    The solution is to set the next node of shorter node as zero node.
    So it will proceed to calculation without effecting result.
    
    """
    ret = ListNode((l1.val + l2.val) % 10)
    carry = (l1.val + l2.val) / 10
    r = ret
    while l1.next or l2.next or carry == 1:
        if l1.next is None:
            l1.next = ListNode(0)
        if l2.next is None:
            l2.next = ListNode(0)
        l1 = l1.next
        l2 = l2.next
        ret.next = ListNode((carry + l1.val + l2.val) % 10)
        carry = (carry + l1.val + l2.val) / 10
        ret = ret.next
    return r
