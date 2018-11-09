class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        l = len(T)
        result = [0 for i in xrange(l)]
        stack = [0]

        for i in xrange(l):
            cur_t = T[i]
            while len(stack) > 0 and T[stack[-1]] < cur_t:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return result
