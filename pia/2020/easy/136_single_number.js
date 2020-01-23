/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
  let map = {};
  let result = 0;
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    if (!map[num]) {
      map[num] = 1;
    } else {
      map[num]++;
    }
  }
  for (let key in map) {
    if (map[key] === 1) {
      return key;
    }
  }
  return -1;
};
