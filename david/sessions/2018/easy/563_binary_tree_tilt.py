# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tilt = 0
        self.helper(root)
        return self.tilt

    def helper(self, root):
        if not root:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        self.tilt += abs(left - right)
        return root.val + left + right

        '''
        First attempt (which should actually be correct...)
        '''
        '''
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val

        val = abs(self.helper(root.left)-self.helper(root.right))
        self.tilt += val
        return val
        '''
