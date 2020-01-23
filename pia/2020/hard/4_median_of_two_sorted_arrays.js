/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
  let merged = [];

  while (nums1.length || nums2.length) {
    if (!nums1.length) {
      merged.push(nums2.shift());
    } else if (!nums2.length) {
      merged.push(nums1.shift());
    } else if (nums1[0] < nums2[0]) {
      merged.push(nums1.shift());
    } else {
      merged.push(nums2.shift());
    }

  }
  const mid = (merged.length - 1) / 2;
  if (mid % 1 === 0) {
    return merged[mid];
  } else {
    return (merged[Math.floor(mid)] + merged[Math.ceil(mid)]) / 2;
  }
};
