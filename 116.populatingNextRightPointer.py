# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        """
        # Method 1

        levelstart = root
        while levelstart:
            cur = levelstart
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                if cur.right and cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            levelstart = levelstart.left
        """
        # Method 2
        p = root
        cur = None
        while p.left:
            cur = p
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            p = p.left
