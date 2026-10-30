function rotate(matrix) {
    
    const n = matrix.length;
    const result = Array.from({ length: n }, () => Array(n).fill(0));

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
        result[j][n - 1 - i] = matrix[i][j];
        }
    }

    return result;
}