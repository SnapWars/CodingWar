class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash = 0
        hold = -prices[0]
        l = len(prices)
        for p in xrange(1, l):
            cash = max(cash, hold + prices[p] - fee)
            hold = max(hold, cash - prices[p])
        return cash
