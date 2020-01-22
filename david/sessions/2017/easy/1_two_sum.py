class Solution(object):
    def twoSum(self, nums, target):
        _map = {}
        for (i, num) in enumerate(nums):
            _map[num] = i

        for (i, num) in enumerate(nums):
            if target - num in _map.keys() and _map[target - num] != i:
                return [i, _map[target - num]]

        return []
