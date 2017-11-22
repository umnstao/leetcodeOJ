class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x > 0:
            sign = 1
        else:
            sign = -1

        x = abs(x)
        result = 0
        while x!= 0:
            tail = x%10
            newresult = result * 10 + tail
            result = newresult
            x = x/10
            if result >= 2147483647:
                return 0
        return result*sign

