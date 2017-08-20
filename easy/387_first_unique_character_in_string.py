class Solution(object):
    def firstUniqChar(self, s):
        count = {}
        for c in s:
            count[c] = 1 if c not in count else count[c] + 1
        for (i, c) in enumerate(s):
            if count[c] == 1:
                return i
        return -1
