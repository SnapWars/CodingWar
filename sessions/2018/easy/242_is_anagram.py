class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for c in s:
            d[c] = 1 if c not in d else d[c] + 1

        for c in t:
            if c not in d or d[c] == 0:
                return False
            d[c] -= 1
        return sum(d.values()) == 0
