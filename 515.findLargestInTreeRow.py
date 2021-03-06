# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = [root]
        ret = []
        while len(queue) > 0:
            size = len(queue)
            levelmax = -float('inf')
            for _ in range(size):
                node = queue.pop(0)
                if node.val > levelmax:
                    levelmax = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret.append(levelmax)
        return ret
