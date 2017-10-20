# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        self.height(root, ret)
        return ret

    def height(self, node, ret):
        if not node:
            return -1
        leftLevel = self.height(node.left, ret)
        rightLevel = self.height(node.right, ret)
        level = 1 + max(leftLevel, rightLevel)
        if len(ret) == level:
            ret.append([])
        ret[level].append(node.val)
        return level

