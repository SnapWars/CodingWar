class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = {'(': ')', '[': ']', '{': '}'}

        for c in s:
            if c in d:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if c != d[top]:
                    return False
        return len(stack) == 0
