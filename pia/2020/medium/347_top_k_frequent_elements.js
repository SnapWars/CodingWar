/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  if (nums.length === k) {
    return nums;
  }
  let map = {};
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    if (!map[num]) {
      map[num] = 1;
    } else {
      map[num]++;
    }
  }
  if (Object.keys(map).length === k) {
    return Object.keys(map);
  }
  let occurences = []; // [key, value]
  for (key in map) {
    occurences.push([key, map[key]]);
  }
  const sorted = occurences.sort((a, b) => b[1] - a[1]);

  let freq = [];
  for (let i = 0; i < k; i++) {
    freq.push(sorted[parseInt(i)][0]);
  }
  return freq;

};



