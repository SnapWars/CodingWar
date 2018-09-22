class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return head

        new_next = head.next
        while new_next and new_next.val == head.val:
            new_next = new_next.next
        head.next = self.deleteDuplicates(new_next)
        return head
