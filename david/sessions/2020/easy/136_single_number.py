'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                s.remove(num)
        
        return list(s)[0]
'''

from functools import reduce

# O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
