class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.n = len(prices)
        self.memo = {}
        if self.n == 0:
            return 0
        def p(i, left=0, ):
            if i >= self.n:
                return 0
            if (i, left) in self.memo:
                return self.memo[(i, left)]
            buy = min(prices[left:i+1])
            profit_sell = 0
            if prices[i] != buy:
                profit_sell = prices[i] - buy + p(i+2, left=i+2) # cooldown
            profit_not_sell = p(i+1, left=left)
            self.memo[(i, left)] = max(profit_sell, profit_not_sell)
            return self.memo[(i, left)]
        return p(i=0)
