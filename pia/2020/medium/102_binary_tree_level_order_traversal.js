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

var levelOrder = function (root) {
  if (!root) {
    return [];
  }

  let tree = [];
  let result = [];

  tree.push(root);

  while (tree.length > 0) {
    const length = tree.length;
    let temp = [];

    for (let i = 0; i < length; i++) {
      const node = tree.shift();
      temp.push(node.val);

      if (node.left) {
        tree.push(node.left);
      }
      if (node.right) {
        tree.push(node.right);
      }
    }
    result.push(temp);
  }
  return result;
};

