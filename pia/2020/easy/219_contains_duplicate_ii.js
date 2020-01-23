/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function (nums, k) {
  let map = {};
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    if (map[num] >= 0 && i - map[num] <= k) {
      return true;
    }
    map[num] = i;
  }
  return false;
};
