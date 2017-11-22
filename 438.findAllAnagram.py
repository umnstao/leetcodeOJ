class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ret = []
        if not s or not p or len(s) == 0 or len(p) == 0:
            return ret
        hash = [0] * 256
        for c in p:
            hash[ord(c) - ord('a')] += 1
        left, right = 0, 0
        counter = len(p)
        while right < len(s):
            if hash[ord(s[right]) - ord('a')] > 0:
                counter -= 1
            hash[ord(s[right]) - ord('a')] -= 1
            right += 1

            if counter == 0:
                ret.append(left)

            if right - left == len(p):
                if hash[ord(s[left]) - ord('a')] >= 0:
                    counter += 1
                hash[ord(s[left]) - ord('a')] += 1
                left += 1

        return ret

