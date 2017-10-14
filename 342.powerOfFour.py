class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool


        # loop
        while num > 0 and num % 4 == 0:
            num = num / 4
        return num == 1
        """
        return num > 0 and num & (num - 1) == 0 and (num - 1) % 3 == 0