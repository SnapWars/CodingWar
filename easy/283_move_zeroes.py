class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        insert = 0
        for i in xrange(l):
            if nums[i] != 0:
                nums[insert] = nums[i]
                insert += 1
        while insert < l:
            nums[insert] = 0
            insert += 1
