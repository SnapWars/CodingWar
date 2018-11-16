class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        d = {}
        l_a = len(A)
        l_b = len(B)

        if l_a != l_b:
            return False
        if l_a == 0 and l_b == 0:
            return True

        first = B[0]
        for i in xrange(l_a):
            c = A[i]
            if c == first and c not in d:
                d[c] = [i]
            elif c in d:
                d[c].append(i)

        if first not in d:
            return False
        for i in d[first]:
            arr = A[i:] + A[:i]
            if arr == B:
                return True
        return False
