# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        left = self.bfs(root, p)
        right = self.bfs(root, q)

        if not left and not right:
            return None
        if not left:
            return q
        if not right:
            return p

        for i, j in reversed(zip(left, right)):
            if i == j:
                return i
        return None

    def bfs(self, root, target):
        q = [root]
        parent = {}
        result = []
        while len(q) > 0:
            node = q.pop()
            if node == target:
                break
            if node.left:
                q.append(node.left)
                parent[node.left] = node
            if node.right:
                q.append(node.right)
                parent[node.right] = node

        cur = target
        while cur in parent:
            result.insert(0, cur)
            cur = parent[cur]
        if cur == root:
            result.insert(0, cur)
        return result
