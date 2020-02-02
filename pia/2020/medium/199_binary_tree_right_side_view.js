/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var rightSideView = function (root) {
  if (!root) {
    return [];
  }
  let list = [root];
  let visible = [];

  while (list.length) {
    const length = list.length;
    let temp = [];


    for (let i = 0; i < length; i++) {
      const node = list.shift();
      temp.push(node.val);

      if (node.left) {
        list.push(node.left);
      }
      if (node.right) {
        list.push(node.right);
      }
    }
    visible.push(temp[temp.length - 1]);
  }
  return visible;
};
