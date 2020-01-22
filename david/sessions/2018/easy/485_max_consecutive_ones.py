class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        cur_best = 0
        for num in nums:
            if num == 0:
                result = max(result, cur_best)
                cur_best = 0
            else:
                cur_best += 1
        result = max(result, cur_best)
        return result
