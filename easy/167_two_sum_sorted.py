class Solution(object):
    def twoSum(self, numbers, target):
        s = set(numbers)
        l = len(numbers)
        def find(value, start, end):
            mid = (start + end) / 2
            if numbers[mid] == value:
                return mid
            elif numbers[mid] > value:
                return find(value, start, mid-1)
            else:
                return find(value, mid+1, end)

        for i in xrange(l):
            if target == 2 * numbers[i] in s:
                return (i+1, i+2)
            elif target - numbers[i] in s:
                return (i+1, find(target - numbers[i], i+1, l)+1)
        return (-1, -1)
