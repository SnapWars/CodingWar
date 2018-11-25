class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = []
        t = []

        for c in S:
            if c != '#':
                s.append(c)
            else:
                if len(s) == 0:
                    continue
                s.pop()

        for c in T:
            if c != '#':
                t.append(c)
            else:
                if len(t) == 0:
                    continue
                t.pop()

        return s == t
