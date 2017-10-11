class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        x = len(needle)
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+x] == needle:
                return i
        return -1