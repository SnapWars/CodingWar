class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        best = float('-inf')

        while left < right:
            m = min(height[left], height[right])
            best = max(best, m * (right - left))
            if height[left] == m:
                left += 1
            else:
                right -= 1
        return best
