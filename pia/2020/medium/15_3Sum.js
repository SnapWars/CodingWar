/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  const triplets = [];

  if (nums.length < 3) {
    return triplets;
  }

  nums.sort((a, b) => a - b);
  const targetSum = 0;

  for (let i = 0; i < nums.length - 2; i++) {
    if (nums[i] > targetSum) {
      break;
    }
    if (i > 0 && nums[i] === nums[i - 1]) {
      continue;
    }

    let j = i + 1;
    let k = nums.length - 1;

    while (j < k) {
      let sum = nums[i] + nums[j] + nums[k];
      if (sum === targetSum) {
        triplets.push([nums[i], nums[j], nums[k]]);

        while (nums[j] === nums[j + 1]) j++;
        while (nums[k] === nums[k - 1]) k--;

        j++;
        k--;
      } else if (sum < targetSum) {
        j++;
      } else {
        k--;
      }
    }
  }
  return triplets;
};
