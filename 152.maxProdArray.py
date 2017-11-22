class Solution(object):
    def maxProduct(self, nums):

        dp_maxprod = nums[0]
        dp_minprod = nums[0]
        maxprod = nums[0]
        for i in range(1,len(nums)):
            tmp = dp_maxprod
            dp_maxprod = max(dp_maxprod*nums[i], dp_minprod*nums[i], nums[i])
            dp_minprod = min(tmp*nums[i], dp_minprod*nums[i], nums[i])
            maxprod = max(maxprod, dp_maxprod)
        return maxprod



