# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        d = {}
        q = [(root, 1)]
        result = []
        while len(q) > 0:
            node, l = q.pop()
            if node:
                if l not in d:
                    d[l] = [node.val]
                else:
                    d[l].append(node.val)
            if node and node.left:
                q.append((node.left, l+1))
            if node and node.right:
                q.append((node.right, l+1))
        for k in sorted(d.keys()):
            result.append(sum(d[k])/float(len(d[k])))
        return result
