class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        directions = [[0,1], [0,-1], [1, 0], [-1, 0], [1,1], [1,-1], [-1,1], [-1,-1]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                liveNeighbors = 0
                for k in range(len(directions)):
                    x = i + directions[k][0]
                    y = j + directions[k][1]
                    if x < 0 or x > len(board)-1 or y < 0 or y > len(board[0])-1:
                        continue
                    if board[x][y] & 1 != 0:
                        liveNeighbors += 1
                if board[i][j] == 0:
                    if liveNeighbors == 3:
                        board[i][j] = 2
                else:
                    if liveNeighbors < 2 or liveNeighbors > 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 3
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = board[i][j] >> 1

