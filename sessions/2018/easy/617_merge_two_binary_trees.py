# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        t = None
        if t1 and t2:
            t = TreeNode(t1.val + t2.val)
            t.left = self.mergeTrees(t1.left, t2.left)
            t.right = self.mergeTrees(t1.right, t2.right)
        elif t1:
            t = TreeNode(t1.val)
            t.left = t1.left
            t.right = t1.right
        elif t2:
            t = TreeNode(t2.val)
            t.left = t2.left
            t.right = t2.right

        return t
