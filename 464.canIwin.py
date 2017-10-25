class Solution(object):

    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        self.memo = {}
        if (maxChoosableInteger+1)*maxChoosableInteger/2 < desiredTotal:
            return False
        return self.helper(range(1, maxChoosableInteger + 1), desiredTotal)

    def helper(self, nums, dt):
        hash = str(nums)
        if hash in self.memo:
            return self.memo[hash]
        if nums[-1] >= dt:
            return True
        for i in range(len(nums)):
            if not self.helper(nums[:i]+nums[i+1:], dt - nums[i]):
                self.memo[hash] = True
                return True
        self.memo[hash] = False
        return False

