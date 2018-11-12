class Solution(object):
    def findMinDifference(self, A):
        minutes = sorted(map(self.convert, A))
        result = float('inf')
        for x, y in zip(minutes, minutes[1:] + minutes[:1]):
            result = min(result, (y - x) % (24 * 60))
        return result

    def convert(self, s):
        h, m = map(int, s.split(':'))
        return h * 60 + m
