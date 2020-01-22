class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {}
        l = len(S)
        for i in xrange(l):
            last[S[i]] = i

        res = []
        left = 0
        right = 0
        for i in xrange(l):
            c = S[i]
            right = max(right, last[c])
            if i == right:
                res.append(right - left + 1)
                left = right + 1
        return res
