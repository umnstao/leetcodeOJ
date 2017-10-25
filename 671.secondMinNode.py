# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        self.res = float('inf')
        self.min = root.val
        self.helper(root)
        if self.res == float('inf'):
            return -1
        else:
            return self.res

    def helper(self, root):
        if not root:
            return
        if root.val == self.min:
            self.helper(root.left)
            self.helper(root.right)
        elif root.val > self.min and root.val < self.res:
            self.res = root.val
            return
        else:
            return


