class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        j = 0
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                i+= 1
            else:
                nums[j] = nums[i]
                j += 1
        return j
