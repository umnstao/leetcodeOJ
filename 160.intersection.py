# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = 0
        lenB = 0
        curA = headA
        while curA:
            curA = curA.next
            lenA += 1
        curB = headB
        while curB:
            curB = curB.next
            lenB += 1
        curA = headA
        curB = headB
        if lenA > lenB:
            k = lenA - lenB
            while k > 0:
                curA = curA.next
                k = k - 1
        elif lenA < lenB:
            k = lenB - lenA
            while k > 0:
                curB = curB.next
                k = k - 1
        while curA:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None









