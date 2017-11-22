class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(1,10):
            self.dfs(i, n , res)
        return res

    def dfs(self,cur, n, res):
        if cur > n:
            return
        res.append(cur)
        for i in range(10):
            if 10*cur + i > n:
                return
            self.dfs(10*cur+i, n, res)

