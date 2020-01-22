class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        self.l = len(price)
        self.price = price
        self.special = special
        self.result = sum([price[i] * needs[i] for i in xrange(self.l)])
        self.memo = {}
        self.helper(tuple(needs))
        return self.result

    def subtract(self, t1, t2):
        lst = []
        for i, j in zip(t1, tuple(t2)):
            lst.append(i - j)
        return tuple(lst)

    def get_need_price(self, n):
        return sum([self.price[i] * n[i] for i in xrange(self.l)])

    def get_special_price(self, s):
        return s[self.l]

    def helper(self, n, p=0):
        if n in self.memo:
            return self.memo[n]

        res = float('inf')
        for i in n:
            if i < 0:
                return res

        for s in self.special:
            t = self.subtract(n, tuple(s[:self.l]))
            res = min(p + self.get_need_price(n),
                      self.helper(t, p + self.get_special_price(tuple(s))))

        self.result = min(self.result, res)
        self.memo[n] = res
        return res

        '''
        Iterative attempt
        '''
        '''
        l = len(price)
        d = {}
        n = tuple(needs)
        for s in special:
            f = False
            lst = []
            for i, j in zip(n, tuple(s[:l])):
                if i < j:
                    f = True
                    break
                lst.append(i - j)

            if not f:
                d[tuple(lst)] = s[l]

        result = sum([price[i] * needs[i] for i in xrange(l)])
        for k in d:
            rem_cost = 0
            for i in xrange(l):
                rem_cost += price[i] * k[i]
            result = min(result, d[k] + rem_cost)
        return result
        '''
