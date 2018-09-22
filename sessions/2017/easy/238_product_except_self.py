class Solution(object):
    def productExceptSelf(self, nums):
        mult = 1
        result = []
        l = len(nums)
        for i in xrange(l):
            result.append(mult)
            mult *= nums[i]
        mult = 1
        for i in xrange(l-1, -1, -1):
            result[i] *= mult
            mult *= nums[i]
        return result
