class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        l = len(A)
        for i in xrange(l):
            A[i] = map(self.invert, self.reverse(A[i]))
        return A

    def reverse(self, l):
        return l[::-1]

    def invert(self, i):
        return i ^ 1
