# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = 0
        cur = head
        while cur:
            cur = cur.next
            l += 1

        mid = l/2 if l % 2 == 1 else int(math.ceil(l/float(2)))
        cur = head
        while mid > 0:
            cur = cur.next
            mid -= 1
        return cur
