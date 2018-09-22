class Solution(object):
    def arrayPairSum(self, nums):
        s = sorted(nums)
        _sum = 0
        for i in xrange(0, len(nums), 2):
            _sum += s[i]
        return _sum
