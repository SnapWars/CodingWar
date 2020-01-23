/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  nums.sort((a, b) => a - b);
  let counter = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== counter) {
      return counter;
    }
    counter++;

  }
  return counter;
};
