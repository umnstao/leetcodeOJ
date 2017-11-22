# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest = None
        diff = float('inf')
        queue = [root]
        while len(queue) > 0:
            node = queue.pop()
            if abs(node.val - target) < diff:
                diff = abs(node.val - target)
                closest = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return closest
