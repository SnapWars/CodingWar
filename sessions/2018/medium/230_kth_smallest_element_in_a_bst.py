# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import heapq

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        l = []
        q = [root]
        while len(q) > 0:
            node = q.pop()
            l.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        heapq.heapify(l)
        result = None
        for _ in xrange(k):
            result = heapq.heappop(l)
        return result
