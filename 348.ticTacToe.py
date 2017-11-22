class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows = [0]*n
        self.cols = [0]*n
        self.diag, self.antidiag = 0, 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """

        toAdd = 1 if player == 1 else -1
        self.rows[row] += toAdd
        self.cols[col] += toAdd

        if row == col:
            self.diag += toAdd
        if row == len(self.rows) - 1 - col:
            self.antidiag += toAdd

        #print diag, antidiag
        if abs(self.rows[row]) == len(self.rows) or \
            abs(self.cols[col]) == len(self.rows) or \
            abs(self.diag) == len(self.rows) or \
            abs(self.antidiag) == len(self.rows):
            return player

        return 0






# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)