import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        negs = map(operator.neg, nums)
        heapq.heapify(negs)

        result = None
        for _ in xrange(k):
            result = heapq.heappop(negs)
        return -result
