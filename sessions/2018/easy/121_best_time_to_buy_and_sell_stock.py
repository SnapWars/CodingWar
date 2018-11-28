class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cash = float('inf')
        profit = 0

        for p in prices:
            cash = min(cash, p)
            profit = max(profit, p - cash)
        return profit
