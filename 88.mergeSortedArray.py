class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p = m-1
        q = n-1
        for i in reversed(range(len(nums1))):
            if p < 0:
                nums1[i] = nums2[q]
                q -= 1
            elif q < 0:
                nums1[i] = nums1[p]
                p -= 1
            elif nums1[p] > nums2[q]:
                nums1[i] = nums1[p]
                p -= 1
            else:
                nums1[i] = nums2[q]
                q -= 1


