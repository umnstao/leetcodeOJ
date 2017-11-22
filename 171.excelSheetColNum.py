class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        digit = 0
        num = 0
        for char in s:
            digit = ord(char) - ord('A') + 1
            num = num*26 + digit
        return num