class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        
        return int((0+l) * (l+1) / 2 - sum(nums))
