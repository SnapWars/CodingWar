class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        s = sorted(A)
        return A == s or A == list(reversed(s))
