class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        a,b = divmod(n-1,26)
        if not a:
            return chr(65+b)
        return self.convertToTitle(a)+chr(65+b)
