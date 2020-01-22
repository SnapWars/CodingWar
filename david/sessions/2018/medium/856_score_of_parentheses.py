'''
Runtime: 20 ms, faster than 100.00% of Python online submissions for Score of Parentheses.
'''

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        l = len(S)
        stack = []
        result = 0
        for i in xrange(l):
            if S[i] == '(':
                stack.append(i)
            else:
                j = stack.pop()
                if len(stack) == 0:›
                    result += self.helper(S[j+1:i])
        return result

    def helper(self, S):
        l = len(S)
        if l == 0:
            return 1

        result = 0
        stack = []
        l = len(S)
        for i in xrange(l):
            if S[i] == '(':
                stack.append(i)
            else:
                j = stack.pop()
                if len(stack) == 0:
                    result += self.helper(S[j+1:i])
        return 2 * result



        '''Attempt at iterative

        stack = []
        result = 0

        for c in S:
            if c == '(':
                if len(stack) == 0:
                    stack.append((0, 1))    # score, multiplier
                else:
                    last = stack[-1]
                    stack.append((last[0], last[1] * 2))
            else:
                top = stack.pop()
                if len(stack) == 0:
                    result += top[0]
                else:
                    stack.append((top[0] * top[1], top[1]))

            print stack
        return result'''
