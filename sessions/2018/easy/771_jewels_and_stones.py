class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        acc = set(list(J))
        for s in S:
            if s in acc:
                count += 1
        return count
