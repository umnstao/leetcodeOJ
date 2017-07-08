class Solution(object):
    def subsets(self, nums):
        ret = []
        if nums is None or len(nums) == 0:
            return ret
        self.helper(nums, ret, [], 0)
        return ret

    def helper(self, nums, ret, path, k):
        ret.append(path[:])
        for i in range(k, len(nums)):
            path += [nums[i]]
            self.helper(nums, ret, path, i+1)
            path.pop()


