class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        def binarySearch(arr, low, high, target):
            if high < low:
                return False
            mid = (low + high)/2
            if arr[mid] > target:
                return binarySearch(arr, low, mid-1, target)
            if arr[mid] < target:
                return binarySearch(arr, mid+1, high, target)
            return True

        for i in xrange(m):
            if target >= matrix[i][0] and target <= matrix[i][n-1] and binarySearch(matrix[i], 0, n-1, target):
                return True
        return False
