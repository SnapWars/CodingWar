class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        max_sell = None
        for price in reversed(prices):
            if not max_sell:
                max_sell = price
            else:
                max_profit = max(max_profit, max_sell - price)
                max_sell = max(max_sell, price)
        return max_profit
