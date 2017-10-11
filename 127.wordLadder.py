class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not wordList or len(wordList) == 0:
            return 0
        wordSet = set([]) # using list will TLE
        for word in wordList:
            wordSet.add(word)

        queue = [beginWord]
        dist = 1
        while len(queue) > 0:
            n = len(queue)
            for _ in range(n):
                curWord = queue.pop(0)
                if curWord == endWord:
                    #print 'a'
                    return dist
                #print curWord, wordList,queue
                self.addNextWord(curWord, queue, wordSet)
            dist += 1
        return 0

    def addNextWord(self, curWord, queue, wordList):
        if curWord in wordList:
            wordList.remove(curWord)
        for i in range(len(curWord)):
            letter = curWord[i]
            for p in "abcdefghijklmnopqrstuvwxyz":
                nextWord = curWord[:i] + p + curWord[i+1:]
                if p == letter:
                    continue
                if nextWord in wordList:
                    queue.append(nextWord)
                    wordList.remove(nextWord) # try to avoid [pot,dot,lot], considering dot, it also considers lot again.
            curWord = curWord[:i] + letter + curWord[i+1:]







