/**
 * recursive
 */

/**
* Definition for singly-linked list.
* function ListNode(val) {
*     this.val = val;
*     this.next = null;
* }
*/
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (curr, next = null, prev = null) {
  if (!curr) {
    return prev;
  }

  next = curr.next;
  curr.next = prev;

  prev = curr;
  curr = next;
  return reverseList(curr, next, prev);
};


/**
 * Iterative
 */

/**
* Definition for singly-linked list.
* function ListNode(val) {
*     this.val = val;
*     this.next = null;
* }
*/
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (curr, next = null, prev = null) {
  if (!curr) {
    return prev;
  }

  next = curr.next;
  curr.next = prev;

  prev = curr;
  curr = next;
  return reverseList(curr, next, prev);
};
