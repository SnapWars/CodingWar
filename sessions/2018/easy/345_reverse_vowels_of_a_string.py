class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = list(s)
        temp = []
        vowels = set(['a','e','i','o','u'])
        for c in lst:
            if c.lower() in vowels:
                temp.insert(0, c)

        i = 0
        l = len(lst)
        for j in xrange(l):
            c = lst[j]
            if c.lower() in vowels:
                lst[j] = temp[i]
                i += 1
        return ''.join(lst)
