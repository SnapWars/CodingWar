# O(2n)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set(nums)
        _dict = {}

        for i, num in enumerate(nums):
            if num not in _dict:
                _dict[num] = [i]
            else:
                _dict[num].append(i)
        
        for num in nums:
            if target == 2 * num:
                if len(_dict[num]) > 1:
                    return [_dict[num][0], _dict[num][1]]
            elif target - num in s:
                return [_dict[num][0], _dict[target-num][0]]
        
        return [0, 0]
'''

# O(n)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set(nums)
        _dict = {}

        for i, num in enumerate(nums):
            if target - num in _dict:
                return [_dict[target - num], i]
            _dict[num] = i
        
        return [0, 0]
'''
