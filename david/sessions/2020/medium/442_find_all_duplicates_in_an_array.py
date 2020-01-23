import heapq

# O(nlogn), no extra space
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        heapq.heapify(nums)
        seen = None
        
        while len(nums) > 0:
            popped = heapq.heappop(nums)
            
            if not seen or seen != popped:
                seen = popped
            elif seen == popped:
                result.append(popped)
        
        return result
