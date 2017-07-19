# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        prev = dummy
        listlen = 0
        while cur:
            cur = cur.next
            listlen += 1
        k = listlen - n
        cur = head
        while k > 0:
            cur = cur.next
            prev = prev.next
            k = k - 1
        prev.next = cur.next
        return dummy.next

    """
    One Pass
    """
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        prev = dummy
        fast = head
        while n > 0:
            n = n-1
            fast = fast.next
        while fast:
            cur = cur.next
            prev = prev.next
            fast = fast.next
        prev.next = cur.next
        return dummy.next

