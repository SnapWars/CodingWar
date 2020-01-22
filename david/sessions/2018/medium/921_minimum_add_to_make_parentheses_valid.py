class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for s in S:
            if s == '(':
                stack.append(s)
            else:
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s)
        return len(stack)
