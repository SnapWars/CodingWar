class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        def helper(nums, step=0):
            if step == len(nums):
                self.result.append(nums)

            for i in xrange(step, len(nums)):
                copy = [num for num in nums]
                copy[step], copy[i] = copy[i], copy[step]
                helper(copy, step + 1)
        helper(nums)
        return self.result
