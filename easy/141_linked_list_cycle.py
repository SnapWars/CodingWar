class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        if head.val == float('inf'):
            return True
        head.val = float('inf')
        return self.hasCycle(head.next)
