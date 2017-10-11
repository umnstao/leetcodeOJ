class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ret = []
        nums.sort()
        self.helper(ret, nums, 0, [])
        return ret
    def helper(self, ret, nums, k, path):
        ret.append(path[:])
        for i in xrange(k, len(nums)):
            if i!= k and nums[i] == nums[i-1]:
                continue
            path += [nums[i]]
            self.helper(ret, nums, i+1, path)
            path.pop()



# sort is necessary.
# check path in ret: cannot distinguish [4,1] and [1,4]
