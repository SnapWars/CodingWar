/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
  digits[digits.length - 1]++;

  let carry = 0;
  for (let i = digits.length - 1; i >= 0; i--) {
    const sum = digits[i] + carry;

    if (sum === 10) {
      digits[i] = sum - 10;
      carry = 1;
    } else {
      digits[i] = sum;
      carry = 0;
    }
  }
  if (carry > 0) {
    digits.unshift(carry);
  }
  return digits;
};
