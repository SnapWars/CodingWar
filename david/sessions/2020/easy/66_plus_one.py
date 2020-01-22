# O(n)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        result = []
        
        for num in reversed(digits):
            num += carry
            
            if num == 10:
                carry = 1
                result.insert(0, 0)
            else:
                carry = 0
                result.insert(0, num)
        
        if carry:
            result.insert(0, 1)

        return result
