class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dict = {}
        for i in range(len(words)):
            w = words[i]
            if w in self.dict:
                self.dict[w].append(i)
            else:
                self.dict[w] = [i]
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ix1 = self.dict[word1]
        ix2 = self.dict[word2]
        i1, i2 = 0, 0
        ret = float('inf')
        while i1 < len(ix1) and i2 < len(ix2):
            ret = min(ret, abs(ix2[i2] - ix1[i1]))          
            if ix1[i1] > ix2[i2]:
                i2 += 1
            else:
                i1 += 1
        return ret
            


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)