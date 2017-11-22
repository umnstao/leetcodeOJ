class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myTable = {}
        for i in range(len(nums)):
            if nums[i] in myTable:
                return [myTable[nums[i]], i]
            else:
                myTable[target - nums[i]] = i


            # {2:0, 7:1, 11:2, 15:3}
