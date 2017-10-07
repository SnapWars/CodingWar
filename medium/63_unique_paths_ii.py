class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        matrix = [[0 for _ in xrange(n)] for _ in xrange(m)]

        for i in xrange(0, n):
            if obstacleGrid[0][i] == 1:
                break
            matrix[0][i] = 1
        for j in xrange(0, m):
            if obstacleGrid[j][0] == 1:
                break
            matrix[j][0] = 1

        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i-1][j] != 1:
                    matrix[i][j] += matrix[i-1][j]
                if obstacleGrid[i][j-1] != 1:
                    matrix[i][j] += matrix[i][j-1]
        return matrix[m-1][n-1]
