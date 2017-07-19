class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """


        """
        The main point of this problem is to establish relationship between courses.
        Use one list of list to illustrate course dependency (previously hashmap for topological sort) for counting out-degree
        Use the other list to count in-degree for BFS when the count is 0.
        """

        if not prerequisites:
            return True
        outDegree = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        for i in range(len(prerequisites)):
            first = prerequisites[i][1]
            second = prerequisites[i][0]
            outDegree[first].append(second)
            inDegree[second] += 1
        result = []
        queue = []
        for i in range(numCourses):
            if inDegree[i] == 0:
                result.append(i)
                queue.append(i)
        while len(queue) > 0:
            course = queue.pop(0)
            for i in outDegree[course]:
                inDegree[i] -= 1
                if inDegree[i] == 0:
                    queue.append(i)
                    result.append(i)
        return len(result) == numCourses

