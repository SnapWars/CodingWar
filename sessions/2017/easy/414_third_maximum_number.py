class Solution(object):
    def thirdMax(self, nums):
        s = set(nums)
        _max = None
        if len(s) < 3:
            return max(s)

        for i in xrange(3):
            _max = max(s)
            s.remove(_max)

        return _max
