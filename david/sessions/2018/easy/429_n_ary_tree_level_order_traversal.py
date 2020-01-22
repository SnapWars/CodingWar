"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = [(root, 0)]
        result = []
        while len(q) > 0:
            node, l = q.pop()
            if len(result) <= l:
                result.append([node.val])
            else:
                result[l].append(node.val)
            for c in node.children[::-1]:
                q.append((c, l+1))
        return result
