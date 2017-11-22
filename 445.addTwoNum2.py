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
        s1 = []
        s2 = []
        while l1 :
            s1.append(l1.val)
            l1 = l1.next
        while l2 :
            s2.append(l2.val)
            l2 = l2.next
        #print s1, s2
        sums = 0
        x = ListNode(0)
        cc = x
        while len(s1) > 0 or len(s2)>0:
            if len(s1) > 0:
                sums += s1.pop()
            if len(s2) > 0:
                sums += s2.pop()
            x.val = sums % 10
            head = ListNode(sums/10)
            head.next = x
            x = head
            sums = sums/10
        return x.next if x.val == 0 else x
