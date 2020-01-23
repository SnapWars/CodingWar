/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function (n, map = {}) {
  if (n === 1) return true;
  const sum = n.toString().split('').reduce((total, num) => {
    return total + Math.pow(parseInt(num), 2);
  }, 0);
  if (map[sum]) return false;

  map[sum] = true;
  return isHappy(sum, map);
};
