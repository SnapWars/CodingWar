'''
Runtime: 20 ms, faster than 100.00% of Python online submissions for Uncommon Words from Two Sentences.
'''

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        s = ' '.join([A, B])
        d = {}

        for word in s.split():
            d[word] = 1 if word not in d else d[word] + 1

        result = []
        for k in d:
            if d[k] == 1:
                result.append(k)
        return result
