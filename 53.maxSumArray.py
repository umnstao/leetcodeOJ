class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = nums[0]
        maxtohere = nums[0]
        for i in range(1,len(nums)):
            maxtohere = max(nums[i], maxtohere + nums[i])
            dp = max(dp, maxtohere)
        return dp