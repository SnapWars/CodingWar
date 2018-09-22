class Solution(object):
    def longestPalindrome(self, s):
        count = {}

        for c in s:
            count[c] = 1 if c not in count else count[c] + 1

        result = 0
        odd = False
        for v in count.values():
            if v % 2 == 0:
                result += v
            else:
                result += v - 1
                odd = True

        return result + 1 if odd else result
