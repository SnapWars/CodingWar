class Solution(object):
    def searchInsert(self, nums, target):
        for i in xrange(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
