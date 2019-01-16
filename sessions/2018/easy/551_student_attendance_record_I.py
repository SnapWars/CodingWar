class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = 0
        i = 0
        while i < len(s):
            streak = 0
            while i < len(s) and s[i] == 'L':
                i += 1
                streak += 1
            result = max(result, streak)
            i += 1
        return s.count('A') <= 1 and result <= 2
