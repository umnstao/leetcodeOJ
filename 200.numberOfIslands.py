class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                if grid[i][j] == '1':
                    self.BFS(grid, i, j)
                    island += 1
        return island

    def BFS(self, grid, a, b):
        queue = [(a,b)]
        rows = [-1, 0, 1, 0]
        cols = [0, -1, 0, 1]
        while len(queue) > 0:
            node = queue.pop()
            for k in range(4):
                x = int(node[0]) + rows[k]
                y = int(node[1]) + cols[k]
                if self.checkValid(grid, x, y):
                    queue.append((x,y))
                    grid[x][y] = '0'

    def checkValid(self, grid, x, y):
        if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[0]) - 1:
            return False
        return grid[x][y] == '1'