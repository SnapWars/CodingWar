"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        q = [(root, 1)]
        result = 1
        while len(q) > 0:
            node, l = q.pop()
            result = max(result, l)
            for c in node.children:
                q.append((c, l+1))
        return result
