class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = len(s) - 1
        l = list(s)

        while left < right:
            temp = l[left]
            l[left] = l[right]
            l[right] = temp
            left += 1
            right -= 1
        return ''.join(l)
