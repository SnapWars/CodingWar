class Solution(object):
    def lengthOfLastWord(self, s):
        l = s.split()
        return 0 if len(l) == 0 else len(l[-1])
