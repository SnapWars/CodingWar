class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        return [word for word in words if self.p(word, pattern)]

    def p(self, word, pattern):
        pd = {}
        wd = {}
        l = len(word)
        for i in xrange(l):
            if pattern[i] not in pd:
                pd[pattern[i]] = word[i]
            else:
                if word[i] != pd[pattern[i]]:
                    return False

            if word[i] not in wd:
                wd[word[i]] = pattern[i]
            else:
                if pattern[i] != wd[word[i]]:
                    return False
        return True
