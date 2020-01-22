class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = {}
        for c in magazine:
            d[c] = 1 if c not in d else d[c] + 1

        for c in ransomNote:
            if c not in d or d[c] == 0:
                return False
            d[c] -= 1
        return True
