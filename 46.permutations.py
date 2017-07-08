class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self.helper(nums, [], ret, 0)
        return ret
    def helper(self, nums, path, ret, k):
        if len(path) == len(nums):
            ret.append(path[:])
        for i in xrange(k, len(nums)):
            if nums[i] in path:
                continue
            path += [nums[i]]
            self.helper(nums, path, ret, 0)
            path.pop()