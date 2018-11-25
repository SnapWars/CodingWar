# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, root, _min, _max):
        if not root:
            return True
        if not _min < root.val < _max:
            return False
        return self.helper(root.left, _min, root.val) and self.helper(root.right, root.val, _max)
