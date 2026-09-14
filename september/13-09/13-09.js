function findMissingNumbers(arr) {

    const bigNumber = Math.max(...arr);
    let missingNumbers = [];

    for(let i = 1; i <= bigNumber; i++){
        if(!arr.includes(i)){
        missingNumbers.push(i);
        }
    }

    return missingNumbers;
}