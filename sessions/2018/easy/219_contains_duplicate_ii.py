class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        l = len(nums)
        for i in xrange(l):
            n = nums[i]
            if n not in d:
                d[n] = [i]
            else:
                if i - d[n][-1] <= k:
                    return True
                d[n].append(i)
        return False
