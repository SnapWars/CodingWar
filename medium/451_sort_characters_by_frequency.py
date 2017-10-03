class Solution(object):
    def frequencySort(self, s):
        d = {}
        d_rev = {}
        result = ''
        for c in s:
            d[c] = 1 if c not in d else d[c] + 1
        for key in d:
            if d[key] not in d_rev:
                d_rev[d[key]] = [key]
            else:
                d_rev[d[key]].append(key)
        for key in sorted(d_rev.keys(), reverse=True):
            for element in d_rev[key]:
                result += element * key
        return result
