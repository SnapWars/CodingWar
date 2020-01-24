/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrderBottom = function (root) {
  if (!root) {
    return [];
  }

  let list = [root];
  let result = [];

  while (list.length) {
    const length = list.length;
    let sublist = [];

    for (let i = 0; i < length; i++) {
      const node = list.shift();
      sublist.push(node.val);

      if (node.left) {
        list.push(node.left);
      }
      if (node.right) {
        list.push(node.right);
      }
    }
    result.unshift(sublist);
  }
  return result;
};
