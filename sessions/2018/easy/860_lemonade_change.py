class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if not bills:
            return True
        d = {}
        for b in bills:
            if b == 5:
                d[5] = 1 if 5 not in d else d[5] + 1
            if b == 10:
                if 5 in d and d[5] > 0:
                    d[5] -= 1
                    d[10] = 1 if 10 not in d else d[10] + 1
                else:
                    return False
            if b == 20:
                if 5 in d and 10 in d and d[5] > 0 and d[10] > 0:
                    d[5] -= 1
                    d[10] -= 1
                elif 5 in d and d[5] >= 3:
                    d[5] -= 3
                else:
                    return False
        return True
