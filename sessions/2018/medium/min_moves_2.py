class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sorted(nums)
        result = 0
        i, j = 0, len(s) - 1
        while i < j:
            result += s[j] - s[i]
            i += 1
            j -= 1
        return result
