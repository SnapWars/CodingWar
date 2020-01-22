class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.coins = coins
        result = self.helper(amount, 0)
        return -1 if result == float('inf') else result

    def helper(self, amount, count):
        print amount, count
        if amount < 0:
            return float('inf')
        if amount == 0:
            return count

        result = float('inf')
        for c in self.coins:
            result = min(result, self.helper(amount - c, count + 1))
        return result
