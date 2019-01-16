class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1 = {}
        d2 = {}
        for n in nums1:
            d1[n] = 1 if n not in d1 else d1[n] + 1
        for n in nums2:
            d2[n] = 1 if n not in d2 else d2[n] + 1

        result = []
        inter = set(nums1).intersection(set(nums2))

        for n in inter:
            for _ in xrange(min(d1[n], d2[n])):
                result.append(n)
        return result
