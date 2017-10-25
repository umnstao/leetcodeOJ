class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        if c < 0:
            return False
        start = 0
        end = int(math.sqrt(c))
        while start  <= end:
            cur = start * start + end * end
            if cur < c:
                start += 1
            elif cur > c:
                end -= 1
            else:
                return True
        return False