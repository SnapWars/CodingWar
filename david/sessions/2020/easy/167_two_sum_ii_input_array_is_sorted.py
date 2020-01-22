# O(2n), higher memory
'''
class Solution:        
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = set(numbers)
        _dict = {}
        
        for i in range(len(numbers)):
            num = numbers[i]
            
            if num not in _dict:
                _dict[num] = [i]
            else:
                _dict[num].append(i)

        for num in numbers:
            if target == 2 * num and len(_dict[num]) == 2:
                return [i+1 for i in _dict[num]]
            elif target - num in s:
                return [_dict[num][0]+1, _dict[target-num][0]+1]
'''

# O(nlogn), lower memory
'''
class Solution:
    def binarySearch(self, numbers, target):
        l = len(numbers)
        mid = int(l/2)

        if numbers[mid] > target:
            return self.binarySearch(numbers[:mid], target)
        elif numbers[mid] < target:
            return mid + 1 + self.binarySearch(numbers[mid+1:], target)
        
        # There is exactly one solution
        return mid
        
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = set(numbers)
        
        for i in range(len(numbers)):
            n = numbers[i]
            if target - n in s:
                return [i+1, i+2+self.binarySearch(numbers[i+1:], target-n)]
    '''

# Meh
'''
class Solution:        
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        left, right = 0, l-1
        
        while left < right:
            sum = numbers[left] + numbers[right]
            
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left += 1
            else:
                right -= 1

        return [0, 0]
'''