# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key = lambda x: x.start)

        ret = []
        tmp = [intervals[0].start, intervals[0].end]
        for i in range(1,len(intervals)):
            if intervals[i].start <= tmp[1]:
                tmp[1] = max(tmp[1],intervals[i].end)
            else:
                ret.append(tmp[:])
                tmp[0] = intervals[i].start
                tmp[1] = intervals[i].end
        ret.append(tmp)
        return ret
