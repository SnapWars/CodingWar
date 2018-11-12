class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        visited = set()
        result = 0
        for i in xrange(l):
            if i not in visited:
                cur = nums[i]
                count = 0
                while nums[cur] not in visited:
                    visited.add(nums[cur])
                    cur = nums[cur]
                    count += 1
                result = max(result, count)
        return result
