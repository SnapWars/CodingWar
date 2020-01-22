class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        _dict = {}
        
        for val in arr:
            _dict[val] = 1 if val not in _dict else _dict[val] + 1
        
        return len(set(_dict.values())) == len(_dict.values())
