class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        m = max(l1, l2)
        num1 = int('0' * (m - l1) + num1)
        num2 = '0' * (m - l2) + num2
        result = 0

        for i in xrange(m):
            n = int(num2[i])
            result += num1 * n * 10 ** (m - 1 - i)
        return str(result)
