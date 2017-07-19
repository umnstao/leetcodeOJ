# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while cur and cur.next:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if prev.next == cur: # keep moving forward
                cur = cur.next
                prev = prev.next
            else: # jump the cur one.
                cur = cur.next
                prev.next = cur
        return dummy.next