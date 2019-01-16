# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0

        h = []
        s = sorted(intervals, key=lambda i: i.start)

        for i in s:
            if not h:
                heapq.heappush(h, i.end)
            else:
                if h[0] <= i.start:
                    heapq.heappop(h)
                heapq.heappush(h, i.end)
        return len(h)
