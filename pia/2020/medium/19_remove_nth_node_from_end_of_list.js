/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }

 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
  let dummy = new ListNode(0);
  dummy.next = head;
  let length = 0;

  let list = head;
  while (list) {
    length++;
    list = list.next;
  }
  list = dummy;
  length -= n;

  while (length > 0) {
    length--;
    list = list.next;
  }
  list.next = list.next.next;
  return dummy.next;
};
