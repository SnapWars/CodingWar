class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        self.grid = grid
        self.h = len(grid)
        self.w = len(grid[0])
        self.adj = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        result = 0
        for i in xrange(self.h):
            for j in xrange(self.w):
                if self.grid[i][j] == '1':
                    self.ff(i, j)
                    result += 1
        return result

    def ff(self, r, c):
        if not 0 <= r < self.h or not 0 <= c < self.w or self.grid[r][c] == '0':
            return
        self.grid[r][c] = '0'
        for dx, dy in self.adj:
            self.ff(r + dx, c + dy)
