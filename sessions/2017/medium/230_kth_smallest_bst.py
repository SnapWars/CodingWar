# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import heapq

class Solution(object):
    def kthSmallest(self, root, k):
        self.vals = []

        def helper(root):
            if not root:
                return
            self.vals.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        heapq.heapify(self.vals)
        result = None
        for _ in xrange(k):
            result = heapq.heappop(self.vals)
        return result
