class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int

        # DFS
        visited = [0]*len(M)
        count = 0
        for i in range(len(M)):
            if visited[i] == 0:
                visited[i] = 1
                self.dfs(visited, M, i)
                count += 1
        return count

    def dfs(self, visited, M, i):
        for j in range(len(M)):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(visited, M, j)
        """
        # Union-Find
        n = len(M)
        leads = [0] * n
        for i in range(len(leads)):
            leads[i] = i

        # union
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j]:
                    leads1 = self.find(i, leads)
                    leads2 = self.find(j, leads)
                    leads[leads1] = leads2

        # find
        flagSet = set()
        for i in range(n):
            flagSet.add(self.find(i, leads))
        return len(flagSet)

    def find(self, x, parents):
        if parents[x] == x:
            return x
        else:
            return self.find(parents[x], parents)

