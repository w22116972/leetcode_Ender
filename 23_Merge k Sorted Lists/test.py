
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists_min_heap(self, lists):
        from heapq import heappop, heappush
        if not lists:
            return None
        tail = head = ListNode(-1)
        min_heap = []
        for node in lists:
            if node:
                heappush(min_heap, (node.val, node))
        return head.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pass

    def mergeKLists_divide(self, lists):
        '''
        Idea: pair up K lists and merge each pair in O(n) (We knew that: Merge
        two sorted lists: T= O(n), S= O(1) )
        - 1st round: There are K/2 lists, each of size is 2 * N
        - 2nd round: There are K/4 lists, each of size is 4 * N
        - nth round: There are K/(2^x) lists, each of size is (2^x) * N

        => k/2 * 2n + k/4 * 4n + ... k/(2^x) * (2^x)n = nk * x
        => x = log_2(k)
        => T = O(nk log(k))

        '''
        i, j = 0, len(lists)  # i從左邊，j從右邊
        while j > 0:
            '''
            當j還沒走到0時，再把i設為0，就可以繼續縮小
            '''
            i = 0
            while i < j:
                '''
                把index從1~n縮成1~n/2，而i跟j也都走到n/2附近
                '''
                lists[i] = self.merge_two_sortedList(lists[i], lists[j])
                i += 1
                j -= 1
        return lists[0]

    def merge_two_sortedList(self, l1, l2):
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

# Solution.mergeKLists