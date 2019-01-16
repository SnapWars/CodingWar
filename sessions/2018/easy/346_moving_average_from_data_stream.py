class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.length = 0
        self.buf = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.length < self.size:
            self.length += 1
        else:
            self.buf.pop(0)
        self.buf.append(val)
        return sum(self.buf)/float(self.length)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
