# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # Divide and Conquer
        if root is None:
            return False
        if root.left is None and root.right is None and sum - root.val == 0:
            return True
        leftCond = self.hasPathSum(root.left, sum - root.val)
        rightCond = self.hasPathSum(root.right, sum - root.val)
        return leftCond or rightCond
        # To check leaf, the condition must be left and right are all none.