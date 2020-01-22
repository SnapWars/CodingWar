class Solution(object):
    def findLongestChain(self, pairs):
        s = pairs.sort(key=lambda x: x[0])
        l = len(pairs)
        self.memo = {}

        def next(offset, end):
            for i, (a, b) in enumerate(pairs[offset:]):
                if a > end:
                    return i + offset
            return -1

        def c(i):
            if i in self.memo:
                return self.memo[i]
            if i >= l or i == -1:
                return 0
            self.memo[i] = max(1+c(next(i+1, pairs[i][1])), c(i+1))
            return self.memo[i]

        return c(0)
