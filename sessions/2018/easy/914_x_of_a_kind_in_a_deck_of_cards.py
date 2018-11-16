from fractions import gcd

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        l = len(deck)
        d = {}
        for i in xrange(l):
            d[deck[i]] = 1 if deck[i] not in d else d[deck[i]] + 1
        _gcd = reduce(lambda x, y: gcd(x, y), d.values())
        return _gcd >= 2
