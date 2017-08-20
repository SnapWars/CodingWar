class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = (1 + n) * n / 2
        return expected_sum - sum(nums)
