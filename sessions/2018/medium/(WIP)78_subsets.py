class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.l = len(nums)
        self.result = []
        visited = set()
        for i in xrange(self.l):
            self.helper(list(nums[i]), nums[:i] + nums[i+1:])
        return self.result

    def helper(self, left, right):
        if len(left) == self.l:
            self.result.append(left)

        for i in xrange(len(right)):
            copy = list(left)
            copy.append(right[i])
            self.helper(copy, right[:i] + right[i+1:])
