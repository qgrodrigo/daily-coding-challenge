function countRectangles(width, height) {

    let count = (width * (width + 1) / 2) * (height * (height + 1) / 2);

    console.log(count);

    return count;
}

// Tests:
countRectangles(1, 3) //should return 6.
countRectangles(3, 2) //should return 18.
countRectangles(1, 2) //should return 3.
countRectangles(5, 4) //should return 150.
countRectangles(11, 19) //should return 12540.