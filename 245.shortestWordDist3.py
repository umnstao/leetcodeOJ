class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1 = -1
        i2 = -1
        ret = float('inf')
        for k in range(len(words)):
            if words[k] == word1:
                i1 = k
            if words[k] == word2:
                if words[k] == word1:
                    i1 = i2
                i2 = k
            if i1 != -1 and i2 != -1:
                ret = min(ret, abs(i1-i2))
        return ret