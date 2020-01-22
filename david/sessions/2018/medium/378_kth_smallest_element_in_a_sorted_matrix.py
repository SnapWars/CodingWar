import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l = list(itertools.chain.from_iterable(matrix))
        heapq.heapify(l)

        result = None
        for _ in xrange(k):
            result = heapq.heappop(l)
        return result
