# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        import numpy as np
        if len(points) <= 0:
            return 0
        if len(points) <= 2:
            return len(points)
        res = 0
        for i in range(len(points)):
            dic = {}
            samex = 1
            samep = 0
            for j in range(0, len(points)):
                if j != i:
                    if points[j].x == points[i].x and points[j].y == points[i].y:
                        samep += 1
                    # cannot compute division
                    if points[j].x == points[i].x:
                        samex += 1
                        continue

                    slope = (points[i].y - points[j].y)* np.longdouble(1) / (points[i].x - points[j].x)
                    if slope not in dic:
                        dic[slope] = 2
                    else:
                        dic[slope] += 1
                    res =  max(res, dic[slope] + samep)
            # compare with the vertical line
            res = max(res, samex)

        return res