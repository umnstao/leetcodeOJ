# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        dummy, cond = self.helper(root)
        return cond

    def helper(self, root):
        if root is None:
            return 0, True
        leftDepth, leftCond = self.helper(root.left)
        rightDepth, rightCond = self.helper(root.right)
        if leftCond is False or rightCond is False:
            return 0, False
        if abs(leftDepth - rightDepth) > 1:
            return 0, False
        else:
            return max(leftDepth, rightDepth)+1, True

# return +1 !!