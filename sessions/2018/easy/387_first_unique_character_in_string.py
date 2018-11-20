class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        l = len(s)
        for i in xrange(l):
            c = s[i]
            d[c] = 1 if c not in d else d[c] + 1

        for i in xrange(l):
            c = s[i]
            if d[c] == 1:
                return i
        return -1
