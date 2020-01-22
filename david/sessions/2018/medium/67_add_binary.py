class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        l_a = len(a)
        l_b = len(b)
        m = max(l_a, l_b)
        if l_a < m:
            a = '0'*(m-l_a) + a
        if l_b < m:
            b = '0'*(m-l_b) + b

        carry = False
        for x, y in reversed(zip(a, b)):
            if x == '0' and y == '1' or x == '1' and y == '0':
                result.insert(0, '1' if not carry else '0')
            elif x == '0' and y == '0':
                result.insert(0, '0' if not carry else '1')
                carry = False
            else:
                result.insert(0, '0' if not carry else '1')
                carry = True
        if carry:
            result.insert(0, '1')
        return ''.join(result)

        '''
        Initial implementation (trivial)
        '''
        '''
        return str(bin(int(a, 2) + int(b, 2)))[2:]
        '''
