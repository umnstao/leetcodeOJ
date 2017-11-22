class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start +1 < end:
            mid = start + (end - start)/2
            cnt = 0
            for i in nums:
                if i <= mid:
                    cnt += 1
            if cnt <= mid:
                start = mid
            else:
                end = mid

        cnt = 0
        for i in nums:
            if i == start:
                cnt += 1
        if cnt > 1:
            return start
        else:
            return end
