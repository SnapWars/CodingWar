class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = set(nums)
        l = len(nums)
        for i in xrange(l):
            if target - nums[i] in s:
                for j in xrange(i+1, l):
                    if nums[j] == target - nums[i]:
                        return [i, j]
