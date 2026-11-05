function buildMatrix(rows, cols) {

    let row = Array(cols).fill(0);
    let filledMatrix = Array(rows).fill(row);

    console.log(filledMatrix);

    return filledMatrix;
}

//Tests
buildMatrix(2, 3) //should return [[0, 0, 0], [0, 0, 0]].
buildMatrix(3, 2) //should return [[0, 0], [0, 0], [0, 0]].
buildMatrix(4, 3) //should return [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]].
buildMatrix(9, 1) //should return [[0], [0], [0], [0], [0], [0], [0], [0], [0]].