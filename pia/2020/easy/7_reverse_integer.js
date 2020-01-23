/**
 * @param {number} x
 * @return {number}
 */
const MAX_INT = Math.pow(2, 31) - 1;
const MIN_INT = -Math.pow(2, 31);

var reverse = function (x) {

  const arr = x.toString().split('');
  let isNegative = false;
  if (arr[0] === '-') {
    arr.shift();
    isNegative = true;
  }
  arr.reverse();
  const str = arr.join('');
  console.debug(arr, str);
  console.debug(MAX_INT, MIN_INT);
  const num = isNegative ? -parseInt(str) : parseInt(str);
  return (num > MAX_INT || num < MIN_INT) ? 0 : num;
};
