# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if left is None and right is None:
            return True
        if left == None and right != None:
            return False
        if left != None and right == None:
            return False
        if left != None and right != None:
            if left.val == right.val:
                return self.helper(left.left, right.right) and self.helper(right.left,left.right)
            else:
                return False

