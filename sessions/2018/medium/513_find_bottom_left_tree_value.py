# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = [(root, 0)]
        _max = 0
        result = root.val
        while len(q) > 0:
            n, l = q.pop()
            if l > _max:
                result = n.val
                _max = l
            if n.right:
                q.append((n.right, l+1))
            if n.left:
                q.append((n.left, l+1))

        return result
