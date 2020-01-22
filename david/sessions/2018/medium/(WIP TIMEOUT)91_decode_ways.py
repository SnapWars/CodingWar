class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.result = 0
        self.helper(s)
        return self.result

    def helper(self, s):
        l = len(s)
        if l == 0:
            self.result += 1
            return
        cur = ''
        for i in xrange(l):
            cur += s[i]
            if int(cur) > 26 or int(cur) == 0:
                return
            self.helper(s[i+1:])
