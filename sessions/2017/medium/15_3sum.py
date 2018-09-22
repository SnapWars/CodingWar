class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        l = len(nums)
        def twoSum(i, target):
            arr = nums[:i] + nums[i+1:]
            s = set()
            for j in xrange(len(arr)):
                arr_set = set(arr[:j] + arr[j+1:])
                num = arr[j]
                if target - num in arr_set:
                    pair = (num, target - num) if num < target - num else (target - num, num)
                    s.add(pair)
            return s

        for i in xrange(l):
            ts = twoSum(i, -nums[i])
            for s in ts:
                tup = None
                if nums[i] >= s[0] and nums[i] <= s[1]:
                    tup = (s[0], nums[i], s[1])
                elif nums[i] > s[1]:
                    tup = (s[0], s[1], nums[i])
                else:
                    tup = (nums[i], s[0], s[1])
                result.add(tup)
        return list(result)
