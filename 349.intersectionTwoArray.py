class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]


        # use two sets, one hash map, O(n)
        n1 = set(nums1)
        n2 = set(nums2)

        hmap = {}
        hlist = []
        for i in n1:
            hmap[i] = 1

        for j in n2:
            if j in hmap:
                hlist.append(j)
        return hlist

        # use two sets, O(n)
        s1 = set()
        intersect = set()
        for i in range(len(nums1)):
            s1.add(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] in s1:
                intersect.add(nums2[i])
        ret = []
        for i in intersect:
            ret.append(i)
        return ret
        """
        # use one set, O(nlogn)
        nums1.sort()
        nums2.sort()
        mySet = set()
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                mySet.add(nums1[i])
                i += 1
                j += 1
        ret = []
        for k in mySet:
            ret.append(k)
        return ret
