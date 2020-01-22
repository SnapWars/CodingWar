class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.g = {}
        self.result = ['JFK']
        for t in tickets:
            f = t[0]
            t = t[1]
            if f not in self.g:
                self.g[f] = {}
            self.g[f][t] = 1 if t not in self.g[f] else self.g[f][t] + 1
        self.dfs('JFK')
        return self.result

    def dfs(self, node):
        if node not in self.g:
            return

        for adj in sorted(self.g[node].keys()):
            if self.g[node][adj] > 0:
                if adj in self.g and len(self.g[adj].keys()) > 0:
                    self.result.append(adj)
                    self.g[node][adj] = max(0, self.g[node][adj] - 1)
                    self.dfs(adj)
                elif sum(self.g[node].values()) == 1:
                    self.result.append(adj)
                    self.g[node][adj] = max(0, self.g[node][adj] - 1)
                    return
