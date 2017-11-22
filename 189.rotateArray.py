class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(0, len(nums) - 1, nums)
        self.reverse(0, k-1, nums)
        self.reverse(k, len(nums) - 1, nums)

    def reverse(self, start, end, nums):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
