class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.glob_k = k
        def helper(k, n):
            if k == 1:
                return [n] if n > 0 and n <= 9 else None
            if n > 9 * k:
                return None
            result = []
            for base in xrange(1, 10):
                h = helper(k-1, n-base)
                if h:
                    if k != self.glob_k:
                        h.insert(0, base)
                    else:
                        for arr in h:
                            arr.insert(0, base)
                    result.append(h)
            return result
        return helper(self.glob_k, n)
