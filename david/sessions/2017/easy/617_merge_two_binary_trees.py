class Solution(object):
    def mergeTrees(self, t1, t2):
        if not t1 and not t2:
            return None

        t3 = TreeNode(0)

        if t1 and t2:
            t3.val = t1.val + t2.val
        elif t1:
            t3.val = t1.val
        elif t2:
            t3.val = t2.val

        t3.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        t3.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)

        return t3
