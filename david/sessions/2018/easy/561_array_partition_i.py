class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sorted(nums)
        res = 0
        for i in xrange(0, len(s), 2):
            res += s[i]
        return res
