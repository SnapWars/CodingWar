# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1 = l1
        cur2 = l2
        carry = 0
        result = None
        cur_result = None
        while cur1 or cur2 or carry == 1:
            _sum = carry
            if cur1:
                _sum += cur1.val
            if cur2:
                _sum += cur2.val

            carry = _sum / 10
            node = ListNode(_sum % 10)
            if not result:
                result = node
                cur_result = result
            else:
                cur_result.next = node
                cur_result = cur_result.next

            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
        return result
