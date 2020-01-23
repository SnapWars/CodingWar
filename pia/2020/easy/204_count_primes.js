/**
 * @param {number} n
 * @return {number}
 */
const isPrime = (num) => {
  if (num <= 1) {
    return false;
  }
  if (num % 2 === 0 && num !== 2) {
    return false;
  }
  const sqrt = Math.sqrt(num);
  for (let i = 2; i <= sqrt; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}

var countPrimes = function (n) {
  let num = 1;
  let counter = 0;

  while (num < n) {
    if (isPrime(num)) {
      counter++;
    }
    num++;
  }
  return counter;
};
