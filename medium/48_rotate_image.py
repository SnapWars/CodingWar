class Solution(object):
    def rotate(self, matrix):
        z = zip(*matrix)
        for i in xrange(len(matrix)):
            matrix[i] = list(z[i][::-1])
