class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        ret = []
        if wordList is None or len(wordList) == 0:
            return ret
        wordSet = set([])
        for word in wordList:
            wordSet.add(word)
        if endWord not in wordSet:
            return ret
        ladders = []
        maps = {}
        distance = {}

        self.bfs(maps, distance, beginWord, endWord, wordSet)
        self.dfs(maps, distance, beginWord, endWord, [], ladders)

        return ladders

    def dfs(self, maps, distance, start, crt, path, ladders):
        path.append(crt)
        #print path, maps, distance
        if crt == start:
            ladders.append(list(reversed(path[:])))
        else:
            for next in maps[crt]:
                #print next
                if next in distance and distance[crt] == distance[next] + 1:
                    self.dfs(maps, distance, start, next, path, ladders)
        path.pop()

    def bfs(self, maps, distance, start, end, dict):
        queue = [start]
        distance[start] = 0
        for word in dict:
            maps[word] = []
        while len(queue) > 0:
            curWord = queue.pop(0)
            nextList = self.expand(curWord, dict)
            #print maps, distance
            for nextWord in nextList:
                maps[nextWord].append(curWord)
                if nextWord not in distance:
                    distance[nextWord] = distance[curWord] + 1
                    queue.append(nextWord)

    def expand(self, curWord, dict):
        expansion = []
        for i in range(len(curWord)):
            letter = curWord[i]
            for p in "abcdefghijklmnopqrstuvwxyz":
                if letter == p:
                    continue
                nextWord = curWord[:i] + p + curWord[i+1:]
                if nextWord in dict:
                    expansion.append(nextWord)
        return expansion

