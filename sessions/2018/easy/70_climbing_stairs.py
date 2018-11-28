class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        a = 1
        b = 1

        for _ in range(2, n+1):
            temp = a + b
            a = b
            b= temp
        return b

    '''
    Initial implementation
    '''
    '''
        self.memo = {1: 1, 2: 2, 3: 3}
        return self.helper(n)

    def helper(self, n):
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n]
    '''
