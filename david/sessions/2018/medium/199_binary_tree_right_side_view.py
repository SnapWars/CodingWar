# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        if not root:
            return result

        q = [(root, 1)]
        level = 0
        while len(q) > 0:
            node, l = q.pop()
            if l > level:
                result.append(node.val)
                level = l
            if node.left:
                q.append((node.left, l + 1))
            if node.right:
                q.append((node.right, l + 1))
        return result
