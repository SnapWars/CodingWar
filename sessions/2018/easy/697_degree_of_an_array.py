class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        l = len(nums)
        rev = nums[::-1]
        for n in nums:
            d[n] = 1 if n not in d else d[n] + 1

        m = max(d.values())
        if m == 1:
            return 1

        keys = [k for k in d if d[k] == m]
        result = float('inf')
        for k in keys:
            start = nums.index(k)
            end = l - 1 - rev.index(k)
            result = min(result, end - start + 1)
        return result
