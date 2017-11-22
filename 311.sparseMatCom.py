class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]

        if A is None or B is None:
            return None
        if len(A[0]) != len(B):
            return None

        c = [ [0 for _ in range(len(B[0]))] for _ in range(len(A))]
        tableA = {}
        tableB = {}
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    if i not in tableA:
                        tableA[i] = {j:A[i][j]}
                    else:
                        tableA[i][j] = A[i][j]

        for i in range(len(B)):
            for j in range(len(B[0])):
                if B[i][j] != 0:
                    if i not in tableB:
                        tableB[i] = {j:B[i][j]}
                    else:
                        tableB[i][j] = B[i][j]

        for i in (tableA.keys()):
            for k in (tableA[i].keys()):
                if k in tableB:
                    for j in (tableB[k].keys()):
                        c[i][j] += tableA[i][k] * tableB[k][j]
        """

        if A is None or B is None:
            return None
        if len(A[0]) != len(B):
            return None

        c = [ [0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for k in range(len(A[0])):
                if A[i][k] != 0:
                    for j in range(len(B[0])):
                        c[i][j] += A[i][k] * B[k][j]

        return c
