class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        l = len(strs)
        if l == 0:
            return []
        result = {}

        for i in xrange(l):
            s = strs[i]
            d = {}
            for c in s:
                d[c] = 1 if c not in d else d[c] + 1
            h = hash(frozenset(d.items()))
            if h not in result:
                result[h] = [s]
            else:
                result[h].append(s)
        return result.values()
        '''
        Naive implementation (times out)
        '''
        '''
        l = len(strs)
        if l == 0:
            return []
        _dict = {}
        result = {}

        for i in xrange(l):
            s = strs[i]
            d = {}
            match = False
            for c in s:
                d[c] = 1 if c not in d else d[c] + 1
            for k in _dict:
                if d == _dict[k]:
                    match = True
                    result[k].append(s)
                    break
            if not match:
                _dict[s] = d
                result[s] = [s]
        return result.values()
        '''
