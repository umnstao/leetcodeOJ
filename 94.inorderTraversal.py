# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        # recursive
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        """
        # iterative
        ret = []
        if not root:
            return ret
        stack = []
        cur = root
        while len(stack) > 0 or cur is not None:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            ret.append(node.val)
            if node.right:
                cur = node.right
        return ret


