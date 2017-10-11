# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        if not lists:
            return None
        dummy = ListNode(-1)
        cur = dummy
        minheap = []
        for ll in list:
            if ll:
                heapq.heappush(minheap, (ll.val, ll))
        while minheap:
            node = heapq.heappop(minheap)[1]
            cur.next = node
            cur = cur.next
            if cur.next:
                heapq.heappush(minheap, (cur.next.val, cur.next))
        return dummy.next




