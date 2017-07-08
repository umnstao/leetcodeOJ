class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        ret = []
        # candidates.sort()
        self.helper(candidates, 0, target, ret, [])
        return ret

    def helper(self, candidates, k, target, ret, path):
        if k >= len(candidates):
            return
        if target < 0:
            return
        if target == 0:
            ret.append(path[:])
            return
        for i in range(k, len(candidates)):
            path += [candidates[i]]
            self.helper(candidates, i, target - candidates[i], ret, path)
            path.pop()
        # If candidates are sorted, but...
        # stop when target < 0 instead of target < candidates[k]
        # because target will become 0 at some point.

        # Array only needs to be sorted because there are duplicates
        # in this Array and one can only use once. (Subset2, combinationSum2, permutaions2)