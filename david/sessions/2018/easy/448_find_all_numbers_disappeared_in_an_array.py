class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)
        l = len(nums)
        result = []
        for i in xrange(1, l+1):
            if i not in s:
                result.append(i)
        return result
