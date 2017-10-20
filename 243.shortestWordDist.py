class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i = -1
        j = -1
        ret = float('inf')
        for k in range(len(words)):
            if words[k] == word1:
                i = k
            if words[k] == word2:
                j = k
            if i != -1 and j != -1:
                ret = min(ret, abs(i-j))
        return ret

