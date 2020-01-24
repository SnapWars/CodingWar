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
var averageOfLevels = function (root) {
  let list = [root];
  let temp = [];
  let result = [];

  let count = 0;
  let sum = 0;
  while (list.length > 0) {
    const node = list.shift();

    sum += node.val;
    count++;

    if (node.left) {
      temp.push(node.left);
    }
    if (node.right) {
      temp.push(node.right);
    }
    if (list.length === 0) {
      result.push(sum / count);
      sum = 0;
      count = 0;
      list = temp;
      temp = [];
    }
  }
  return result;
};
