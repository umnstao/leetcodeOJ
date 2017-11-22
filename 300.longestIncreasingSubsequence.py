class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        T = [0]*len(nums)
        for i in range(len(nums)):
            T[i] = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    T[i] = max(T[j] + 1, T[i])
        longest = 0
        for i in range(len(nums)):
            longest = max(longest, T[i])
        return longest