# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Runtime: 24 ms, faster than 99.94% of Python online submissions for Binary Tree Paths.
'''
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.result = []
        self.dfs(root)
        return self.result

    def dfs(self, root, s=''):
        if not root:
            return

        if not root.left and not root.right:
            self.result.append(s + str(root.val))
            return

        s_app = s + str(root.val) + '->'
        if root.left:
            self.dfs(root.left, s_app)
        if root.right:
            self.dfs(root.right, s_app)
