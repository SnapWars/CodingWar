'''
Runtime: 36 ms, faster than 99.81% of Python online submissions for Permutations.
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.l = len(nums)
        self.result = []
        for i in xrange(self.l):
            self.helper([nums[i]], nums[:i] + nums[i+1:])
        return self.result

    def helper(self, left, right):
        if len(left) == self.l:
            self.result.append(left)
        else:
            for i in xrange(len(right)):
                copy = list(left)
                copy.append(right[i])
                self.helper(copy, right[:i] + right[i+1:])
