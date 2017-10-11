class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        queue = []

        for i in range(len(board)):
            for j in range(len(board[i])):
                if word[0] == board[i][j]:
                    if self.dfs(board, word, 0, i, j):
                        return True
        return False



    def dfs(self, board, word, start, pos_x, pos_y):
        if start == len(word) :
            return True
        if pos_x < 0 or pos_x >= len(board) or pos_y < 0 or pos_y >= len(board[0]):
            return False
        if board[pos_x][pos_y] != word[start]:
            return False

        if board[pos_x][pos_y] == word[start]:
            tmpVal = board[pos_x][pos_y]
            #print tmpVal
            board[pos_x][pos_y] = '#'
            res = self.dfs(board, word, start + 1, pos_x+1, pos_y) or self.dfs(board, word, start + 1, pos_x-1, pos_y) or self.dfs(board, word, start + 1, pos_x, pos_y+1) or self.dfs(board, word, start + 1, pos_x, pos_y-1)
            board[pos_x][pos_y] = tmpVal

        return res