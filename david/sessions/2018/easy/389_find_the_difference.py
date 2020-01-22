class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}

        for c in t:
            d[c] = 1 if c not in d else d[c] + 1

        for c in s:
            if c in d:
                d[c] -= 1

        for k in d:
            if d[k] == 1:
                return k
        return None
