class Solution(object):
    def reverseVowels(self, s):
        vowels = set(['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'])
        vowel_indices = []
        l = list(s)

        for i in xrange(len(s)):
            if s[i] in vowels:
                vowel_indices.append(i)

        rev = vowel_indices[::-1]
        for i in xrange(len(vowel_indices)):
            l[vowel_indices[i]] = s[rev[i]]

        return ''.join(l)
