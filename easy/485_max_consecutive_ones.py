class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        _max = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0

            if count > _max:
                _max = count

        return _max
        
