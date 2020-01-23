/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function (nums, target) {
  if (target <= nums[0]) {
    return 0;
  }
  if (target > nums[nums.length - 1]) {
    return nums.length;
  }

  for (let i = 1; i < nums.length; i++) {
    const curr = nums[i];

    if (curr === target) {
      return i;
    }

    const left = nums[i - 1];
    if (target > left && target < curr) {
      return i;
    }
  }
};
