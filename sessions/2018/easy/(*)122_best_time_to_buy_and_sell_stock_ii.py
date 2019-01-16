class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        l = len(prices)

        for i in xrange(l-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit
