class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        cur = 1
        m = min([len(s) for s in strs])

        for i in xrange(m):
            s = set([s[:cur] for s in strs])
            if len(s) != 1:
                break
            cur += 1
        return strs[0][:cur-1]
