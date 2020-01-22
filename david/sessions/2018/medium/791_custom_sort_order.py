class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        d = {}
        res = ''
        for c in T:
            d[c] = 1 if c not in d else d[c] + 1

        for c in S:
            if c in d:
                res += c*d[c]
                d.pop(c)

        for k in d.keys():
            res += k*d[k]

        return res
