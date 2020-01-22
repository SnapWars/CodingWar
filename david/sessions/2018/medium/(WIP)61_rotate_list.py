# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        l = 0
        cur = head
        tail = None
        while cur:
            l += 1
            if cur.next:
                cur = cur.next
            else:
                tail = cur
                break

        d, r = divmod(k, l)

        cur = head
        while r > 0:
            r -= 1
            cur = cur.next
        if cur == head:
            return head

        next = cur.next
        cur.next = None
        tail.next = head
        return next
