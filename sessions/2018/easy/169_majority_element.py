class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        l = len(nums)
        for n in nums:
            d[n] = 1 if n not in d else d[n] + 1

        for k in d:
            if d[k] > l / 2:
                return k
