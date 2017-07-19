# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        cur = head
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while cur:
            if cur.val == val: # jump the cur one.
                cur = cur.next
                prev.next = cur
            else: # keep moving forward
                cur = cur.next
                prev = prev.next
        return dummy.next





