class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        d, r = divmod(k, l)

        i = l - r
        arr = nums[i:] + nums[:i]
        for a in xrange(len(arr)):
            nums[a] = arr[a]
