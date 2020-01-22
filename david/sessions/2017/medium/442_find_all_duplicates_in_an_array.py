class Solution(object):
    def findDuplicates(self, nums):
        s = set()
        result = []
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                result.append(num)
        return result
