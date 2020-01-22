import heapq

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        heapq.heapify(nums)

        last = None
        result = []
        while len(nums) > 0:
            cur = heapq.heappop(nums)
            if cur == last:
                result.append(cur)
            last = cur
        return result
