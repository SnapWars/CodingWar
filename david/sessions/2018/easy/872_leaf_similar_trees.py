# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.sequence(root1) == self.sequence(root2)

    def sequence(self, root):
        q = [root]
        result = []
        while len(q) > 0:
            node = q.pop()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            if not node.left and not node.right:
                result.append(node.val)
        return result
