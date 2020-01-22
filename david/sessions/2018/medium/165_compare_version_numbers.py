class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l1 = map(int, version1.split('.'))
        l2 = map(int, version2.split('.'))

        m = min(len(l1), len(l2))
        diff = abs(len(l1) - len(l2))
        if len(l1) == m:
            for _ in xrange(diff):
                l1.append(0)
        elif len(l2) == m:
            for _ in xrange(diff):
                l2.append(0)
        for i, j in zip(l1, l2):
            if i > j:
                return 1
            elif i < j:
                return -1
        return 0
