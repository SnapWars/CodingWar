class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        l = len(A)
        i = 0

        while i + 1 < l and A[i] < A[i+1]:
            i += 1

        if i == 0 or i == l-1:
            return False

        while i + 1 < l and A[i] > A[i+1]:
            i += 1

        return i == l-1

        '''
        First attempt
        '''
        '''
        if l < 3:
            return False

        m = max(A)
        return A[1:l-1].count(m) == 1 and A[l-1] != m and A[0] != m
        '''
