class Solution(object):
    def __init__(self):
        self.infinity = False

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        g = {i: set() for i in xrange(numCourses)}
        stack = []
        visited = {i: 0 for i in xrange(numCourses)}
        for a, b in prerequisites:
            g[b].add(a)

        def topoUtil(u):
            if visited[u] == 1:
                self.infinity = True
                return
            elif visited[u] == 0:
                visited[u] = 1
                for v in g[u]:
                    topoUtil(v)
                visited[u] = 2
                stack.append(u)

        def topo():
            result = []
            for i in xrange(numCourses):
                topoUtil(i)
            while not self.infinity and stack:
                result.append(stack[-1])
                stack.pop()
            return result
        return topo()
