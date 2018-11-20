class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p2s = {}
        s2p = {}
        s = str.split()
        l = len(s)
        if len(pattern) != l:
            return False
        for i in xrange(l):
            if pattern[i] not in p2s:
                p2s[pattern[i]] = s[i]
            else:
                if p2s[pattern[i]] != s[i]:
                    return False
            if s[i] not in s2p:
                s2p[s[i]] = pattern[i]
            else:
                if pattern[i] != s2p[s[i]]:
                    return False

        return True
