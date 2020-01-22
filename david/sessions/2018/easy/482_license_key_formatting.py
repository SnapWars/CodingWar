class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = (''.join(S.split('-'))).upper()
        i = len(s)
        result = []
        while i >= 0:
            p = s[max(0, i-K):i]
            if p:
                result.insert(0, p)
            i -= K
        return '-'.join(result)
