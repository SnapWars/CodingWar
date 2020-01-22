class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None

        cum = 0
        best = float('-inf')

        for num in nums:
            if cum + num < num:
                cum = num
            else:
                cum += num
            best = max(best, cum)
        return best

        '''
        Initial implementation
        '''
        '''
        if len(nums) == 0:
            return None

        cum = 0
        best = float('-inf')

        for num in nums:
            cum = cum + num
            best = max(best, cum, num)
            if num == best:
                cum = num
        return best
        '''
