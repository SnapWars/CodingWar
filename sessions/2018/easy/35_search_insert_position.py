class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)

        if target > max(nums):
            return l
        if target < min(nums):
            return 0
        for i in xrange(l):
            if nums[i] == target:
                return i
            if i + 1 < l and nums[i+1] > target:
                return i + 1
        
