# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        q = [(root,1)]
        result = 1
        while len(q) > 0:
            node, l = q.pop()
            result = max(result, l)
            if node and node.left:
                q.append((node.left, l+1))
            if node and node.right:
                q.append((node.right, l+1))
        return result
