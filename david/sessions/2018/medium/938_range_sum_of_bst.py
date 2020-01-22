# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        q = [root]
        result = 0
        while len(q) > 0:
            n = q.pop()
            if n.val >= L and n.val <= R:
                result += n.val
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return result
