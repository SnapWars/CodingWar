class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l = k
        n2f = {}
        f2n = {}
        result = []

        for n in nums:
            n2f[n] = 1 if n not in n2f else n2f[n] + 1

        for k in n2f.keys():
            v = n2f[k]
            if v not in f2n:
                f2n[v] = [k]
            else:
                f2n[v].append(k)

        s = set(f2n.keys())
        while l > 0:
            if len(s) == 0:
                break
            _max = max(s)
            result += f2n[_max]
            l -= len(f2n[_max])
            s.remove(_max)

        return result
