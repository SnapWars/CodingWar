import heapq

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def neg(n):
            return -n

        l = map(neg, list(set(nums)))
        heapq.heapify(l)
        result = None
        for _ in xrange(3):
            if len(l) == 0:
                return max(nums)
            result = heapq.heappop(l)
        return -result
