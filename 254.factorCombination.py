class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ret = []
        self.helper(ret, [], n, 2)
        return ret

    def helper(self, ret, item, n, start):
        upper = int(math.sqrt(n))
        for i in range(start, upper+1):
            if n % i == 0 and n/i >= i:
                item.append(i)
                item.append(n/i)
                ret.append(item[:])
                item.pop()
                self.helper(ret, item, n/i, i)
                item.pop()
        # 12 / 2 = 6
        # 6 / 2 = 3