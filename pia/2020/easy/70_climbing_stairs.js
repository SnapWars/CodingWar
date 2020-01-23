/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n, map = {}) {
  let value = null;

  if (n in map) {
    return map[n];
  } else if (n <= 2) {
    return n;
  } else {
    value = climbStairs(n - 1, map) + climbStairs(n - 2, map);
  }
  map[n] = value;
  return value;
};
