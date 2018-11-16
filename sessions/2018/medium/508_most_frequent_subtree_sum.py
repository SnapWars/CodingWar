# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        self.d = {}
        self.helper(root)
        result = []
        m = max(self.d.values())
        for k in self.d:
            if self.d[k] == m:
                result.append(k)
        return result


    def helper(self, root):
        if not root:
            return 0
        s = root.val + self.helper(root.left) + self.helper(root.right)
        self.d[s] = 1 if s not in self.d else self.d[s] + 1
        return s
