class Solution(object):
    def canWinNim(self, n):
        return n % 4 != 0

    '''def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        self.memo = {1: True, 2: True, 3: True}
        return self.helper(n)

    def helper(self, n):
        if n in self.memo:
            return self.memo[n]

        self.memo[n] = not self.helper(n-1) or not self.helper(n-2) or not self.helper(n-3)
        return self.memo[n]'''
