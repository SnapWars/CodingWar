class Solution(object):
    def uniquePaths(self, m, n):
        matrix = [[0 for _ in xrange(n)] for _ in xrange(m)]

        for i in xrange(0, n):
            matrix[0][i] = 1
        for j in xrange(0, m):
            matrix[j][0] = 1

        for i in xrange(1, m):
            for j in xrange(1, n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

        return matrix[m-1][n-1]
