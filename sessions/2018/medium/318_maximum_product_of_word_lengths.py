class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        l = len(words)
        s = [set(word) for word in words]
        result = 0
        for i in xrange(l):
            for j in xrange(i+1, l):
                inter = s[i].intersection(s[j])
                if len(inter) == 0:
                    result = max(result, len(words[i]) * len(words[j]))
        return result
