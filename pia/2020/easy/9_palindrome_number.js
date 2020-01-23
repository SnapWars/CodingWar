/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  if (x < 0) {
    return false
  }
  const arr = x.toString().split('');

  const length = Math.floor(arr.length / 2);
  for (let i = 0; i < length; i++) {
    const isEqual = arr[i] === arr[arr.length - 1 - i];
    if (!isEqual) {
      return false;
    }
  }
  return true;
};
