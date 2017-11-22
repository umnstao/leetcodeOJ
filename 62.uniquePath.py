class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        p = [[0 for b in range(n)] for a in range(m)]
        for i in range(0,m):
            for j in range(0,n):
                if i == 0 or j == 0:
                    p[i][j] = 1
                else:
                    p[i][j] = p[i-1][j]+p[i][j-1]

        return p[m-1][n-1]