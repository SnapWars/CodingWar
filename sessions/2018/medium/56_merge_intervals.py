# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        l = len(intervals)
        result = []

        if l <= 1:
            return intervals

        s = sorted(intervals, key = lambda x : x.start)
        cur = 0

        while cur < l:
            cur_interval = s[cur]
            while cur < l - 1 and s[cur+1].start >= cur_interval.start and s[cur+1].start <= cur_interval.end:
                cur_interval = Interval(
                    cur_interval.start,
                    max(cur_interval.end, s[cur+1].end)
                )
                cur += 1
            result.append(cur_interval)
            cur += 1
        return result
            
