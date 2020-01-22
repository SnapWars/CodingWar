class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        l = len(flowerbed)
        for i in xrange(l):
            if n == 0:
                break
            num = flowerbed[i]
            if num == 0:
                if i >=1 and flowerbed[i-1] == 1 or i < l - 1 and flowerbed[i+1] == 1:
                    continue
                flowerbed[i] = 1
                n -= 1
        return n == 0
