/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (numbers, target) {
  const map = {};
  for (let i = 0; i < numbers.length; i++) {
    map[numbers[i]] = i;
  }
  for (let i = 0; i < numbers.length; i++) {
    const num = numbers[i];
    const difference = target - num;

    if (map[difference]) {
      return [i + 1, map[difference] + 1];
    }
  }
};
