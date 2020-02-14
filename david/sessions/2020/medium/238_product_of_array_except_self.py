class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        result = []

        for num in nums:
            result.append(left)

            left = left * num

        for i in reversed(range(len(nums))):
            if i != len(nums) - 1:
                result[i] = result[i] * right

            right = right * nums[i]
        
        return result
