class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        self.m = len(grid)
        self.n = len(grid[0])
        self.visited = set()

        def ff(x, y):
            if x < 0 or x >= self.m or y < 0 or y >= self.n:
                return 0
            if grid[x][y] == '0' or (x, y) in self.visited:
                return 0
            self.visited.add((x, y))
            return 1 + ff(x+1, y) + ff(x-1, y) + ff(x, y+1) + ff(x, y-1)

        _count = 0
        for i in xrange(self.m):
            for j in xrange(self.n):
                if ff(i, j) > 0:
                    _count += 1
        return _count
