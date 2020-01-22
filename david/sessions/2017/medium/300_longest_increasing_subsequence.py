class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.l = len(nums)
        self.memo = {}
        def lis(i):
            if i in self.memo:
                return self.memo[i]
            if i > self.l:
                return 0
            if i < self.l-1:
                if nums[i] == nums[i+1]:
                    self.memo[i] = lis(i+1)
                    return self.memo[i]
            _max = 1
            for j in xrange(i+1, self.l):
                if nums[j] > nums[i]:
                    _max = max(_max, 1 + lis(j))
            self.memo[i] = _max
            return self.memo[i]
        result = 0
        for i in xrange(self.l):
            result = max(result, lis(i))
        return result
