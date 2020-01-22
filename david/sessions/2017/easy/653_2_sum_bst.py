# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        q = [root]
        visited = set()
        vals = {}

        while q:
            node = q.pop(0)
            if node not in visited:
                vals[node.val] = 1 if node.val not in vals else vals[node.val] + 1
                visited.add(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        for val in vals:
            if k-val in vals:
                if k != 2 * val or vals[k-val] > 1:
                    return True
        return False
