/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function (nums) {
  const map = {};
  const dupes = [];
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    if (map[num]) {
      dupes.push(num);
    } else {
      map[num] = true;
    }
  }
  return dupes;
};
