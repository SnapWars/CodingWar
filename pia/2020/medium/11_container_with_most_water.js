/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let max = 0;
  let i = 0;
  let j = height.length - 1;

  while (j > i) {
    const h1 = height[i];
    const h2 = height[j];
    const area = Math.min(h1, h2) * (j - i);

    max = Math.max(area, max);

    if (h2 > h1) {
      i++
    } else {
      j--;
    }
  }
  return max;
};
