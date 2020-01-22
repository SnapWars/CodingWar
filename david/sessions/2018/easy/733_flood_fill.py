class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.image = image
        self.h, self.w = len(self.image), len(self.image[0])
        self.start = self.image[sr][sc]
        self.newColor = newColor

        if self.start == self.newColor:
            return self.image

        self.ff(sr, sc)
        return self.image

    def ff(self, r, c):
        if r < 0 or r >= self.h or c < 0 or c >= self.w:
            return
        if self.image[r][c] == self.start:
            self.image[r][c] = self.newColor
            self.ff(r+1, c)
            self.ff(r, c+1)
            self.ff(r-1, c)
            self.ff(r, c-1)
