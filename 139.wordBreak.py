class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = (len(s)+1)*[False]
        dp[0] = True
        for i in range(len(s)+1):
            if dp[i] == True:
                for j in range(i+1, len(s)+1):
                    if s[i:j] in wordDict:
                        dp[j] = True
        return dp[len(s)]