# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        dicts = {}
        dicts[None] = None
        cur = head
        while cur:
            node = RandomListNode(cur.label)
            dicts[cur] = node
            cur = cur.next
        cur = head
        while cur:
            dicts[cur].next = dicts[cur.next] # dicts[cur.next] could be None
            dicts[cur].random = dicts[cur.random]
            cur = cur.next
        return dicts[head]