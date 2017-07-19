# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        dummy = ListNode(-1)
        dummy.next = head
        start = dummy
        for i in range(m-1):
            start = start.next
        prev = start.next
        cur = prev.next
        k = n - m
        while k > 0:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            k = k - 1
        start.next.next = cur
        start.next = prev
        return dummy.next

