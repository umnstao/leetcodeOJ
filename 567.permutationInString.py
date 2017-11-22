class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not s1 or not s2 or len(s1) == 0 or len(s2) == 0:
            return False
        map = [0]*256
        for c in s1:
            map[ord(c) - ord('a')] += 1
        counter = len(s1)
        left, right = 0, 0
        while right < len(s2):
            if map[ord(s2[right]) - ord('a')] > 0:
                counter -= 1
            map[ord(s2[right]) - ord('a')] -= 1
            right += 1

            if counter == 0:
                return True

            if right - left == len(s1):
                if map[ord(s2[left]) - ord('a')] >= 0:
                    counter += 1
                map[ord(s2[left]) - ord('a')] += 1
                left += 1

        return False



