class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def eval(a, op, b):
            if op == '*':
                return a * b

            if a < 0:
                return - (- a / b)
            return a / b

        stack = []
        l = len(s)
        i = 0
        op = None

        while i < l:
            prev = i
            while i < l and (s[i].isdigit() or s[i].isspace()):
                i += 1
            val = int(s[prev:i])

            if op == '*' or op == '/':
                stack.append(eval(stack.pop(), op, val))
            elif op == '-':
                stack.append(-val)
            else:
                stack.append(val)

            if i >= l:
                break

            op = s[i]
            i += 1
        return sum(stack)
