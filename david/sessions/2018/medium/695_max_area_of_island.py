class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.h = len(grid)
        self.w = len(grid[0])
        _max = 0
        for i in xrange(self.h):
            for j in xrange(self.w):
                if grid[i][j] == 1:
                    _max = max(_max, self.ff(i, j))
        return _max

    def ff(self, i, j):
        if i >= self.h or i < 0 or j >= self.w or j < 0:
            return 0
        if self.grid[i][j] == 0:
            return 0

        self.grid[i][j] = 0
        return 1 + self.ff(i-1, j) + self.ff(i, j-1) + self.ff(i+1, j) + self.ff(i, j+1)
