class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        visited = set()
        max_island = 0

        def ff(x, y):
            if x >= m or x < 0 or y >= n or y < 0:
                return 0
            if grid[x][y] == 0 or (x, y) in visited:
                return 0
            visited.add((x, y))
            return 1 + ff(x+1, y) + ff(x, y+1) + ff(x-1, y) + ff(x, y-1)

        for i in xrange(m):
            for j in xrange(n):
                max_island = max(max_island, ff(i, j))
        return max_island
