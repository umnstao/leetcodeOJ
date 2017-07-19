class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mydic = {}
        for c in s:
            if c in mydic:
                mydic[c] += 1
            else:
                mydic[c] = 1
        count = 0
        for i in mydic.values():
            count += i%2
        return count <= 1
