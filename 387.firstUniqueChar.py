class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        myTable = {}
        for c in s:
            if c in myTable:
                myTable[c] += 1
            else:
                myTable[c] = 1
        for i in range(len(s)):
            if myTable[s[i]] == 1:
                return i
        return -1

