class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        l = len(S)
        a = ord('a')
        z = ord('z')
        A = ord('A')
        Z = ord('Z')
        markers = set()
        s = ''
        result = ''

        for i in xrange(l):
            o = ord(S[i])
            is_alpha = a <= o <= z or A <= o <= Z
            if not is_alpha:
                markers.add(i)
            else:
                s += S[i]

        s = s[::-1]
        s_i = 0
        for i in xrange(l):
            if i in markers:
                result += S[i]
            else:
                result += s[s_i]
                s_i += 1
        return result
