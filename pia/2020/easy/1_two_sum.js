/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let indices = [];
  const numsMap = {};

  for (let i = 0; i < nums.length; i++) {
    const currNum = nums[i];
    numsMap[currNum] = i;
  }

  for (let i = 0; i < nums.length; i++) {
    const difference = target - nums[i];
    const doesComplementExist = !!numsMap[difference];
    if (doesComplementExist && numsMap[difference] !== i) {
      return [i, numsMap[difference]];
    }
  }
};
