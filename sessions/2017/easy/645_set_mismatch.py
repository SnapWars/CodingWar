class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        s = set(nums)
        expected_sum = (1 + n) * n / 2
        count = {}
        duplicate = None
        for num in nums:
            count[num] = 1 if num not in count else count[num] + 1
            if count[num] == 2:
                duplicate = num
                break

        missing = expected_sum - sum(s)
        return [duplicate, missing]
