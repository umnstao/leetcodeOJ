class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        p = [[0 for b in range(n)] for a in range(m)]
        for i in range(0,m):
            for j in range(0,n):

                if i == 0 or j == 0:
                    p[i][j] = 1

                else:
                    p[i][j] = p[i-1][j]+p[i][j-1]

                if obstacleGrid[i][j] == 1:
                    p[i][j] = 0

        return p[m-1][n-1]