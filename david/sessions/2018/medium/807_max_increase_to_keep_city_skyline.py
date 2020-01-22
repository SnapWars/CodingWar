class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        l = len(grid)
        r_max = [0 for i in xrange(l)]
        c_max = [0 for i in xrange(l)]

        for r in xrange(l):
            for c in xrange(l):
                r_max[r] = max(r_max[r], grid[r][c])
                c_max[c] = max(c_max[c], grid[r][c])

        diff = 0
        for r in xrange(l):
            for c in xrange(l):
                diff += min(r_max[r], c_max[c]) - grid[r][c]
        return diff
