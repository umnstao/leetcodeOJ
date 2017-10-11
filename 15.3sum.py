class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #O(nlogn) time, no extra space
        ret = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            start = i+1
            end = len(nums) - 1
            while start < end:
                tmpSum = nums[start] + nums[end]
                if tmpSum == target:
                    ret.append([nums[i], nums[start],nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    end -= 1
                    while start < end and nums[end] == nums[end+1]:
                        end -= 1
                elif tmpSum < target:
                    start += 1
                else:
                    end -= 1
        return ret

