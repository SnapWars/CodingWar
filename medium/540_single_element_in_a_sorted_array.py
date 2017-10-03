class Solution(object):
    def singleNonDuplicate(self, nums):
        return reduce(operator.xor, nums, 0)
