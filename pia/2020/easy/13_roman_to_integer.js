const map = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
};

/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {


  if (s.length === 1) {
    return map[s];
  }

  let sum = 0;
  let i = 0;
  const arr = s.split('').reverse();

  // side effect: modifies: sum, arr
  const subtract = (numeral) => {
    while (arr[0] && arr[0] === numeral) {
      sum -= map[numeral];
      arr.shift();
    }
  };

  while (arr[0]) {
    const val = map[arr[0]];

    sum += val;
    const prevChar = arr.shift();

    if (prevChar === 'V' || prevChar === 'X') {
      subtract('I');
    }
    if (prevChar === 'L' || prevChar === 'C') {
      subtract('X');
    }
    if (prevChar === 'D' || prevChar === 'M') {
      subtract('C');
    }

  }

  return sum;
};
