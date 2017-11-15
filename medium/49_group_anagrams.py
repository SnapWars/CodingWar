class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        for s in strs:
            f = {}
            for c in s:
                f[c] = 1 if c not in f else f[c] + 1
            k = frozenset(f.items())
            if k not in d:
                d[k] = []
            d[k].append(s)
        return [d[k] for k in d]
