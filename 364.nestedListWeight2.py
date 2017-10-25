# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSumInverse(self, nestedList):

        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if not nestedList or len(nestedList) == 0:
            return 0
        dd = self.depth(nestedList)
        #print dd
        return self.helper(nestedList, 0, dd)

        # compute Depth
    def depth(self, nestedList):
        if len(nestedList) == 1 and nestedList[0].isInteger():
            return 1
        dd = 0
        for element in nestedList:
            if element.getInteger():
                dd = max(dd, 1)
            else:
                dd = max(self.depth(element.getList()) + 1, dd)
        return dd

        # compute Value

    def helper(self, nestedList, depth, dd):
        val = 0
        for element in nestedList:
            if element.isInteger():
                val += (dd - depth) * element.getInteger()
            else:
                val += self.helper(element.getList(), depth + 1, dd)
        return val




        """
        unweighted = 0
        weighted = 0

        #BFS
        while nestedList:
            #print len(nestedList)
            nextLevel = []
            for element in nestedList:
                print element.isInteger()
                if element.isInteger():
                    unweighted += element.getInteger()
                else:
                    nextLevel.extend(element.getList())
            weighted += unweighted
            nestedList = nextLevel
        return weighted
        """
