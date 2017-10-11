class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start = 1
        end = x
        while start + 1 < end:
            mid = (start + end)/2

            if mid ** 2 <= x:
                start = mid
            else:
                end = mid
        if end ** 2 <= x:
            return end
        else:
            return start


