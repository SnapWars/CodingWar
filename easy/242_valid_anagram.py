class Solution(object):
    def isAnagram(self, s, t):
        s_count = {}
        t_count = {}

        for c in s:
            s_count[c] = 1 if c not in s_count else s_count[c] + 1
        for c in t:
            t_count[c] = 1 if c not in t_count else t_count[c] + 1

        return s_count == t_count
