class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        l = len(nums)
        left = 0
        right = 0
        pivot = -1
        for i in reversed(xrange(l)):
            right += nums[i+1] if i+1 < l else 0
            left = s - nums[i] - right
            if left == right:
                pivot = i
        return pivot
