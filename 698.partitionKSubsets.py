class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        by ...
        """
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
        if sums % k != 0:
            return False
        visited = [False] * len(nums)
        return self.helper(0, k, nums, visited, 0, sums/k)

    def helper(self, startIdx, k, nums, visited, curSum, target):
        print k
        if k == 1:
            return True
        if curSum == target:
            return self.helper(0, k-1, nums, visited, 0, target)
        for i in range(startIdx, len(nums)):
            if visited[i] == False:
                visited[i] = True
                if self.helper(i+1, k, nums, visited, curSum + nums[i], target):
                    return True
                visited[i] = False
        return False

