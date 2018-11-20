class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        expected = (1 + l) * l / 2
        d = {}
        for n in nums:
            d[n] = 1 if n not in d else d[n] + 1
        diff = expected - sum(set(nums))
        for k in d:
            if d[k] == 2:
                break
        return [k, diff]
