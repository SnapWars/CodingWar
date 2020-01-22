'''
Runtime: 32 ms, faster than 99.69% of Python online submissions for Top K Frequent Words.
'''
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        w2f = {}
        f2w = {}
        result = []

        for w in words:
            w2f[w] = 1 if w not in w2f else w2f[w] + 1

        for w in w2f:
            if w2f[w] not in f2w:
                f2w[w2f[w]] = set([w])
            else:
                f2w[w2f[w]].add(w)

        counter = k
        for k in reversed(sorted(f2w.keys())):
            if counter == 0:
                break
            for w in sorted(f2w[k]):
                if counter == 0:
                    break
                counter -= 1
                result.append(w)
        return result
