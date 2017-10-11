class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start = 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == 0:
                nums[left],nums[start] = nums[start],nums[left]
                start += 1
                left += 1
            elif nums[left] == 1:
                left += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1