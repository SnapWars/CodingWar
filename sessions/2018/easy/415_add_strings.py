class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(self.get(num1) + self.get(num2))

    def get(self, num):
        l = len(num)
        base = 1
        result = 0
        for i in reversed(xrange(l)):
            result += int(num[i]) * base
            base *= 10
        return result
