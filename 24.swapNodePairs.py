# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        prev = dummy
        while cur and cur.next:
            next = cur.next
            prev.next = next
            cur.next = next.next
            next.next = cur

            prev = prev.next.next
            cur = cur.next
        return dummy.next
        # 1, 2, 3, 4
        # 1, 3, 2, 4


