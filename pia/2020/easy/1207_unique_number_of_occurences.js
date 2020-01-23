/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function (arr) {
  const occurences = {};
  for (let i = 0; i < arr.length; i++) {
    const num = arr[i];
    if (!occurences[num]) {
      occurences[num] = 1;
    } else {
      occurences[num]++;
    }
  }


  const keys = Object.keys(occurences);
  const map = {};
  for (let i = 0; i < keys.length; i++) {
    const num = occurences[keys[i]];
    if (map[num]) {
      return false;
    } else {
      map[num] = true;
    }
  }
  return true;
};
