import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        d = {}
        d_mir = {}
        result = []
        for num in nums:
            d[num] = 1 if num not in d else d[num] + 1
        for key in d:
            if d[key] not in d_mir:
                d_mir[d[key]] = []
            d_mir[d[key]].append(key)
        keys = map(operator.neg, d_mir.keys())
        heapq.heapify(keys)
        while len(keys) > 0 and k > 0:
            key = -heapq.heappop(keys)
            for i in d_mir[key]:
                result.append(i)
                k -= 1
                if k == 0:
                    break
        return result
