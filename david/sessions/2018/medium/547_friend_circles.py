
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        l = len(M)
        g = {i: [] for i in xrange(l)}
        visited = set()
        result = 0

        for i in xrange(l):
            for j in xrange(l):
                if M[i][j] == 1 and i != j:
                    g[i].append(j)
                    g[j].append(i)

        for i in xrange(l):
            if i not in visited:
                visited.add(i)
                q = [i]
                while len(q) > 0:
                    n = q.pop()
                    for j in g[n]:
                        if j not in visited:
                            visited.add(j)
                            q.append(j)
                result += 1

        return result
