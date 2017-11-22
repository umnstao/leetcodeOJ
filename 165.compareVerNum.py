class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        m, n = len(version1), len(version2)
        i, j = 0, 0

        while i < m or j < n:
            nums1, nums2 = 0, 0
            while i < m and version1[i] != '.':
                nums1 = int(version1[i]) - int('0') + nums1*10
                i += 1
            while j < n and version2[j] != '.':
                nums2 = int(version2[j]) - int('0') + nums2*10
                j += 1
            if nums1 < nums2:
                return -1
            elif nums1 > nums2:
                return 1
            i += 1
            j += 1
        return 0