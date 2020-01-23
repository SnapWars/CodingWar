/**
 * @param {number[][]} mat
 * @param {number} K
 * @return {number[][]}
 */
var matrixBlockSum = function (mat, K) {
  let answer = [];

  for (let i = 0; i < mat.length; i++) {
    const row = mat[i];
    let answerRow = [];
    for (let j = 0; j < row.length; j++) {
      const minI = Math.max(0, i - K);
      const maxI = Math.min(mat.length - 1, i + K);
      const minJ = Math.max(0, j - K);
      const maxJ = Math.min(row.length - 1, j + K);
      let sum = 0;
      for (let r = minI; r <= maxI; r++) {
        for (let c = minJ; c <= maxJ; c++) {
          sum += mat[r][c];
        }
      }
      console.debug('i', minI, maxI, 'j', minJ, maxJ, 'sum', sum);

      answerRow.push(sum);
    }
    answer.push(answerRow);
  }
  return answer;
};
