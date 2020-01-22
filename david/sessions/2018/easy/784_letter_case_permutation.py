class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        self.l = len(S)
        self.s = S
        self.result = []
        self.helper()
        return self.result

    def helper(self, s='', left=0):
        if left == self.l:
            self.result.append(s)

        if left >= self.l:
            return

        if self.s[left].isalpha():
            self.helper(s + self.s[left].lower(), left + 1)
            self.helper(s + self.s[left].upper(), left + 1)
        else:
            self.helper(s + self.s[left], left + 1)
