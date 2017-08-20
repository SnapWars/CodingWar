class Solution(object):
    def reverseWords(self, s):
        l = s.split()
        return ' '.join([w[::-1] for w in l])
