# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        extra = 0
        dummy = ListNode(-1)
        cur = dummy
        while l1 or l2:
            if l1 is None and l2 is not None:
                digit = l2.val + extra
            elif l2 is None and l1 is not None:
                digit = l1.val + extra
            else:
                digit = l1.val + l2.val + extra
            if digit >= 10:
                extra = 1
                digit = digit - 10
            else:
                extra = 0
            node = ListNode(digit)
            cur.next = node
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if extra == 1:
            cur.next = ListNode(1)
        return dummy.next

