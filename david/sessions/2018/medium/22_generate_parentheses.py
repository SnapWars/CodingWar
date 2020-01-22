class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.n = n
        self.result = []
        self.helper()
        return self.result

    def helper(self, s='', left=0, right=0):
        if left + right == 2 * self.n:
            self.result.append(s)
        if left < self.n:
            self.helper(s+'(', left+1, right)
        if right < left:
            self.helper(s+')', left, right+1)
