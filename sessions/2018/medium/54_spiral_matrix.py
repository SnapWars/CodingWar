class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []

        if not matrix:
            return result

        h = len(matrix)
        w = len(matrix[0])

        i = j = 0
        offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        l = 0
        r = w - 1
        u = 0
        d = h - 1
        count = 0
        while count < w * h:
            for k in xrange(4):
                while u <= i <= d and l <= j <= r:
                    o = offsets[k]
                    result.append(matrix[i][j])
                    count += 1
                    i += o[0]
                    j += o[1]
                if k == 0:
                    j = r
                    u += 1
                    i = u
                elif k == 1:
                    i = d
                    r -= 1
                    j = r
                elif k == 2:
                    j = l
                    d -= 1
                    i = d
                elif k == 3:
                    i = u
                    l += 1
                    j = l
        return result
