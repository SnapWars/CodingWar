class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        l = s.lower()
        filt = ''.join([c for c in l if c.isalnum()])
        return filt == filt[::-1]
