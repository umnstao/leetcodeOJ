class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [ [False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        dp[0][0] = True
        """
        for i in range(1, len(s)+1):
            dp[i][0] = False
        """

        for j in range(1, len(p)+1):
            if p[j-1] == '*':
                dp[0][j] = True
            else:
                break

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    if s[i-1] == p[j-1] or p[j-1] == '?':
                        dp[i][j] = dp[i-1][j-1]
        #print dp
        return dp[-1][-1]