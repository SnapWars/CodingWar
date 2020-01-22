# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.memo = {}

    def rob(self, root):
        if not root:
            return 0
        if root in self.memo:
            return self.memo[root]
        gc_left = 0
        gc_right = 0
        if root.left:
            gc_left = self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            gc_right = self.rob(root.right.left) + self.rob(root.right.right)

        self.memo[root] = max(root.val + gc_left + gc_right, self.rob(root.left) + self.rob(root.right))
        return self.memo[root]
