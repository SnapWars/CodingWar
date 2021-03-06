class Solution(object):
    def merge(self, intervals):
        result = []
        for interval in sorted(intervals, key=lambda i: i.start):
            if len(result) > 0 and interval.start <= result[-1].end:
                result[-1].end = max(result[-1].end, interval.end)
            else:
                result.append(interval)
        return result
