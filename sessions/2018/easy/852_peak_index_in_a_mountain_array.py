class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        m = max(A)
        l = len(A)
        for i in xrange(l):
            if A[i] == m:
                return i
