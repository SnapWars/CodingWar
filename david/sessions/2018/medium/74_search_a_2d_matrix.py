'''
Runtime: 20 ms, faster than 100.00% of Python online submissions for Search a 2d Matrix.
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        h = len(matrix)
        if h == 1:
            return target in matrix[0]

        w = len(matrix[0])
        for row in matrix:
            if row[0] <= target <= row[w-1]:
                return self.searchMatrix([row], target)

        return False
