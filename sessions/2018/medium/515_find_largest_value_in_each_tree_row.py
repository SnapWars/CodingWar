# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        d = {}
        q = [(root, 0)]

        while len(q) > 0:
            p, l = q.pop(0)

            if not p:
                continue
            if l not in d:
                d[l] = p.val
            else:
                d[l] = max(d[l], p.val)

            if p.left:
                q.append((p.left, l+1))
            if p.right:
                q.append((p.right, l+1))

        return [d[k] for k in sorted(d.keys())]
