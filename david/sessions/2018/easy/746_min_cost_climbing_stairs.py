class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        self.memo = {}
        return self.helper(cost)

    def helper(self, cost, index=0):
        if index in self.memo:
            return self.memo[index]

        l = len(cost)
        if l == 2:
            return min(cost)
        if l == 3:
            return min(cost[0] + self.helper(cost[1:]), cost[1])
        else:
            self.memo[index] = min(
                cost[0] + self.helper(cost[1:], index + 1),
                cost[1] + self.helper(cost[2:], index + 2)
            )
            return self.memo[index]
