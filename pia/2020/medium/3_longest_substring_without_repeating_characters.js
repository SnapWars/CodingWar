/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let maxLength = 0;
  let curr = 0;
  let map = {};

  if (s.length < 2) {
    return s.length;
  }
  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    if (map[char] == null) {
      curr++;
    } else {
      curr = Math.min(i - map[char], curr + 1);
    }
    maxLength = Math.max(maxLength, curr);
    map[char] = i;
  }
  return maxLength;
};
