# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        if not root:
            return result

        q = [(root, False)]
        while len(q) > 0:
            node, left = q.pop()
            if left and not node.left and not node.right:
                result += node.val
            if node.right:
                q.append((node.right, False))
            if node.left:
                q.append((node.left, True))
        return result
