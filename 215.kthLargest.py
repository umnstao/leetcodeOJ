class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        return self.helper(nums, k, 0, len(nums)-1)

    def helper(self, nums, k, start, end):
        if start == end:
            return nums[start]
        pivot = nums[(start + end)/2]
        left = start
        right = end
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -=1
            if left <= right:
                nums[left], nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
        if right - start + 1 >= k:
            return self.helper(nums, k, start, right)
        elif left - start < k:
            return self.helper(nums, k- (left - start), left, end)
        else:
            return nums[right + 1]


        """
        import heapq
        hhh = []
        for i in range(len(nums)):
            heapq.heappush(hhh, nums[i])
            if len(hhh) > k:
                heapq.heappop(hhh)
        hhh.sort(reverse = True)
        return hhh[-1]

        return self.helper(nums, k, 0, len(nums)-1)

    def helper(self, nums, k, start, end):
        if start == end:
            return nums[start]
        pivot = nums[(start+end)/2]
        left = start
        right = end
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if right - start + 1 >= k:
            return self.helper(nums, k, start, right)
        elif left - start + 1 <= k:
            #print left, end, nums[end]
            return self.helper(nums, k - (left-start), left, end)
        else:
            return nums[right + 1]

        """
