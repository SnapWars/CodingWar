import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = map(self.neg, nums)
        heapq.heapify(l)
        result = None
        for _ in xrange(k):
            result = heapq.heappop(l)
        return -result

    def neg(self, i):
        return -i
