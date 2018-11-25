class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        plus = 1
        l = len(digits)
        for i in reversed(xrange(l)):
            digits[i] += plus + carry
            plus = 0
            carry = digits[i] / 10
            digits[i] %= 10
        if carry > 0:
            digits.insert(0, carry)
        return digits
