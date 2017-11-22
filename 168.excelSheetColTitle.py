class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        ret = []
        while n > 0:
            ret.append(capitals[ (n-1)%26 ])
            n = (n-1) / 26
        ret.reverse()
        return ''.join(ret)