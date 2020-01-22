import heapq

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxs=heapq.nlargest(3, nums)
        mins=heapq.nsmallest(2, nums)

        return max(maxs[0]*maxs[1]*maxs[2], maxs[0]*mins[0]*mins[1])
