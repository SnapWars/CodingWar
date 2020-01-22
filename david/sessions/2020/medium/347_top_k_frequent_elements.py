# O(n + logn + klogn)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        forward = {}
        
        for num in nums:
            forward[num] = 1 if num not in forward else forward[num] + 1
        
        return heapq.nlargest(k, forward.keys(), key=forward.get)
