class Solution(object):
    def singleNumber(self, nums):
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                s.remove(num)
        return list(s)
