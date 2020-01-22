class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
