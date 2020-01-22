# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if head and not head.next:
            return head

        oh, ot, eh, et = self.helper(head, head.next)
        ot.next = eh
        return oh

    def helper(self, odd, even):
        oh, ot = odd, odd
        eh, et = even, even

        while ot and ot.next:
            ot_next = ot.next.next
            et_next = None if not ot_next else ot_next.next
            ot.next = ot_next
            et.next = et_next
            ot = ot_next if ot_next else ot
            et = et_next if et_next else et
        return (oh, ot, eh, et)
