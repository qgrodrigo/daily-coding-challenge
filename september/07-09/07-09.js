function parseRomanNumeral(numeral) {
  
    const romans = {I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000};

    let sum = 0;

    for (let index = 0; index < numeral.length -1; index++) {

        if (romans[numeral[index]] < romans[numeral[index +1]] ) {
            sum -= romans[numeral[index]];
        } else {
            sum += romans[numeral[index]];
        }
    }
  
  sum += romans[numeral[numeral.length -1]]

  //console.log(sum)
  return sum;
}