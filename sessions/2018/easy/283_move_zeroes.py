class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l == 0:
            return
        d = {}
        cursor = l - 1
        order = []
        for i in xrange(l):
            if nums[i] == 0:
                while cursor > 0 and nums[cursor] == 0:
                    cursor -= 1
                if i < cursor:
                    d[i] = cursor
                    cursor -= 1
            else:
                order.append(nums[i])

        for k in d:
            temp = nums[k]
            nums[k] = nums[d[k]]
            nums[d[k]] = temp
        if len(d) == 0:
            return
        l = len(order)
        nums[:l] = order
