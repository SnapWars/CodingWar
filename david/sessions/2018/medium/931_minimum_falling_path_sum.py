class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        self.l = len(A)
        for i in reversed(xrange(self.l-1)): # ignore last row
            for j in xrange(self.l):
                A[i][j] = A[i][j] + min(
                    self.get_val(A, i+1, j-1),
                    self.get_val(A, i+1, j),
                    self.get_val(A, i+1, j+1)
                )
        return min(A[0])

    def get_val(self, A, i, j):
        if i < 0 or i >= self.l or j < 0 or j >= self.l:
            return float('inf')
        return A[i][j]
