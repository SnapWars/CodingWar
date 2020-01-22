class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s2t = {}
        t2s = {}
        l_s = len(s)
        l_t = len(t)
        if l_s == 0 and l_t == 0:
            return True
        if l_s != l_t:
            return False

        for i in xrange(l_s):
            if s[i] not in s2t:
                s2t[s[i]] = t[i]
            else:
                if s2t[s[i]] != t[i]:
                    return False
            if t[i] not in t2s:
                t2s[t[i]] = s[i]
            else:
                if t2s[t[i]] != s[i]:
                    return False
        return True
