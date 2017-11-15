class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        self.memo = {}
        def m(i):
            if i in self.memo:
                return self.memo[i]
            if i >= l:
                return 0
            self.memo[i] = max(nums[i] + m(i+2), m(i+1))
            return self.memo[i]
        return m(0)
