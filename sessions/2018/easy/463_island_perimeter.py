class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.result = 0
        self.grid = grid
        self.h = len(grid)
        self.w = len(grid[0])
        self.offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.visited = set()

        for i in xrange(self.h):
            for j in xrange(self.w):
                self.ff(i, j)
        return self.result

    def get(self, r, c):
        if not 0 <= r < self.h or not 0 <= c < self.w:
            return 0
        return self.grid[r][c]

    def ff(self, r, c):
        if (r, c) in self.visited:
            return
        val = self.get(r, c)
        if val == -1 or val == 0:
            return
        count = sum([self.get(r + dx, c + dy) for dx, dy in self.offsets])
        self.result += 4 - count
        self.visited.add((r, c))
