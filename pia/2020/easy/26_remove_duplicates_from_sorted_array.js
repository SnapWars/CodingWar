/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  let map = {};

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    if (!map[num]) {
      map[num] = true;
    } else {
      nums.splice(i, 1);
      i--;
    }
    // console.debug(num, map)

  }
  return nums.length;
};
