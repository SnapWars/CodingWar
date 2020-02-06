/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function (root) {
  return explore(root, 0);
};

function explore(node, currDepth) {
  if (!node) {
    return currDepth;
  }
  let leftDepth = explore(node.left, currDepth + 1);
  let rightDepth = explore(node.right, currDepth + 1);
  return Math.max(leftDepth, rightDepth);
}
