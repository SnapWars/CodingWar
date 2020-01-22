# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        cur = head
        s = set(G)
        cur_s = set()
        result = 0
        while cur:
            if cur.val in s:
                cur_s.add(cur.val)
            else:
                if len(cur_s.intersection(s)) > 0:
                    result += 1
                cur_s = set()
            cur = cur.next
        if len(cur_s.intersection(s)) > 0:
            result += 1
        return result
