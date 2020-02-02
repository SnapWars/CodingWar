/**
 *
 * Hash map solution
 */

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function (nums1, nums2) {
  const nums1Map = {};
  for (let i = 0; i < nums1.length; i++) {
    const num = nums1[i]
    if (!nums1Map[num]) {
      nums1Map[num] = 1;
    }
  }

  let result = [];
  for (let i = 0; i < nums2.length; i++) {
    const num = nums2[i];
    if (nums1Map[num] === 1) {
      result.push(num);
      nums1Map[num]++;
    }
  }
  return result;
};


/**
 * Set solution
 */


/**
* @param {number[]} nums1
* @param {number[]} nums2
* @return {number[]}
*/
var intersection = function (nums1, nums2) {
  const set = new Set(nums1);
  return [...new Set(nums2.filter(num => set.has(num)))]
};
