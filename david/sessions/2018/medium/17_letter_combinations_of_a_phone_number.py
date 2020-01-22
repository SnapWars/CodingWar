'''
Runtime: 20 ms, faster than 100.00% of Python online submissions for Letter Combinations of a Phone Number.
'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.result = []
        self.l = len(digits)
        if self.l == 0:
            return []
        self.helper(digits, 0)
        return self.result

    def helper(self, digits, length, build=''):
        if length == self.l:
            self.result.append(build)
            return
        for c in self.map[digits[0]]:
            self.helper(digits[1:], length + 1, build + c)
