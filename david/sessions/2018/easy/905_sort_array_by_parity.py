class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        for a in A:
            if a % 2 == 0:
                even.append(a)
            else:
                odd.append(a)
        return even + odd
