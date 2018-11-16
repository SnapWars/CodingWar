"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        q = [(root, False)]
        result = []
        while len(q) > 0:
            node, ch_visited = q.pop()
            result.append(node.val)
            if ch_visited:
                continue
            for c in reversed(node.children):
                for ch in reversed(c.children):
                    q.append((ch, False))
                q.append((c, True))
        return result
