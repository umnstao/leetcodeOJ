class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

        #O(m+n) space
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return
        queue = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    queue.append((i,j))

        while len(queue) > 0:
            x1,x2 = queue.pop(0)
            for j in range(len(matrix[0])):
                matrix[x1][j] = 0
            for i in range(len(matrix)):
                matrix[i][x2] = 0
        """
        #O(1) space
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return
        fr = False
        fc = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if i == 0:
                        fr = True
                    if j == 0:
                        fc = True
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if fr:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if fc:
            for i in range(len(matrix)):
                matrix[i][0] = 0



