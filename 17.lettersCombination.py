class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        charmap = [0, 1, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ret = []
        self.helper(charmap, digits, "", 0, ret)
        return ret

    def helper(self, charmap, digits, path, idx, ret):
        if len(digits) == len(path):
            ret.append(path)
        for i in range(idx, len(digits)):
            digit = ord(digits[i]) - ord('0')
            astr = charmap[digit]
            for s in astr:
                self.helper(charmap, digits, path + s, i+1, ret)
