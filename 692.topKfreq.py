class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __eq__(self, other):
        return self.count == other.count and self.word == other.word

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        import heapq

        res = []
        map = {}
        # O(n) space
        for i in range(len(words)):
            if words[i] in map:
                map[words[i]] += 1
            else:
                map[words[i]] = 1

        pq = []
        for word, count in map.items():
            heapq.heappush(pq, (Element(count,word), word))
            if len(pq) > k:
                heapq.heappop(pq)

        for _ in range(k):
            res.append(heapq.heappop(pq)[1])
        return res[::-1]