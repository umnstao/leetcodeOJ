class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
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

