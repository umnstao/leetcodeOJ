class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sa = 0
        for i in range(0,len(nums)):
            sa += nums[i]
        sb = (1+len(nums))*len(nums)/2
        return sb-sa
