/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const search = (nums, target, l, r) => {
  if (l > r) {
    return [-1, -1];
  }
  const mid = (l + r) / 2;
  if (nums[mid] < target) {
    return search(nums, target, mid + 1, r);
  }
  if (nums[mid] > target) {
    return search(nums, target, l, mid - 1);
  }
  if (nums[l] < target) {
    return search(nums, target, l + 1, r);
  }
  if (nums[r] > target) {
    return search(nums, target, l, r - 1);
  }
  return [l, r];
};

var searchRange = function (nums, target) {
  if (nums.length === 0) {
    return [-1, -1];
  }

  let l = 0;
  let r = nums.length - 1;
  return search(nums, target, l, r);
};
