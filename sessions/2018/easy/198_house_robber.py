class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.memo = {}
        return self.helper(nums)

    def helper(self, nums, index=0):
        if index in self.memo:
            return self.memo[index]

        l = len(nums)
        if not l:
            return 0
        if l == 1:
            return nums[0]

        self.memo[index] = max(
            nums[0] + self.helper(nums[2:], index+2),
            self.helper(nums[1:], index + 1)
        )
        return self.memo[index]
