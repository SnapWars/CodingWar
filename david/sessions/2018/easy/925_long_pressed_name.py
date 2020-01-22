class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        n = self.helper(name)
        t = self.helper(typed)
        if len(n) != len(t):
            return False
        for x, y in zip(n, t):
            if x[0] != y[0] or x[1] > y[1]:
                return False
        return True

    def helper(self, s):
        result = []
        prev = None
        counter = 1
        l = len(s)

        for i in xrange(l):
            c = s[i]
            if not prev:
                prev = c
                counter = 1
            elif c != prev:
                result.append((prev, counter))
                prev = c
                counter = 1
            else:
                counter += 1

            if i == l - 1:
                result.append((prev, counter))
        return result
