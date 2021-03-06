# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def equals(s,t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            return s.val == t.val and equals(s.left, t.left) and equals(s.right,t.right)

        def traverse(s,t):
            return s != None and (equals(s,t) or traverse(s.left,t) or traverse(s.right,t))

        return traverse(s,t)
