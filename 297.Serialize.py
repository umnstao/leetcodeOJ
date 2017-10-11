# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return '{}'
        queue = [root]

        index = 0
        while index < len(queue):
            if queue[index] is not None:
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index += 1
        #print queue
        # record the value
        data = []
        for i in range(len(queue)):
            if queue[i] is None:
                data.append('#')
            else:
                data.append(str(queue[i].val))

        # transform to string
        strData = ','.join(data)
        strData = '{'+strData+'}'
        return strData

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '{}':
            return None

        data = data[1:-1].split(',')
        root = TreeNode(int(data[0]))
        queue = [root]

        isLeftChild = True
        isRightChild = False

        index = 0
        for i in xrange(1, len(data)):
            if data[i] != '#':
                node = TreeNode(int(data[i]))
                if isLeftChild:
                    queue[index].left = node
                else:
                    queue[index].right = node
                queue.append(node)
            if not isLeftChild:
                index += 1
            isLeftChild = not isLeftChild

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))