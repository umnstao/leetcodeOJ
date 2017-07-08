class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return nums
        if len(nums) == 0:
            return [[]]
        nums.sort()
        ret = []
        used = [False]*len(nums)
        self.helper(nums,ret,[],used)
        return ret

    def helper(self, nums, ret, path,used):
        if len(path) == len(nums):
            ret.append(path[:])
            #print path
        for i in range(len(nums)):
            if used[i]:
                continue
            if i>0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            used[i] = True
            path += [nums[i]]
            self.helper(nums, ret, path,used)
            used[i] = False
            path.pop()