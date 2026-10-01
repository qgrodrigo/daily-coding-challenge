function toDecimal(binary) {

    binary = binary.split("").reverse().join('');
    let decimal = 0;

    for(let i = 0 ; i < binary.length; i++){

        decimal += parseInt(binary[i]) * (2 ** i);

    }

    console.log(decimal) 


    return binary;
}

toDecimal("101") //should return 5.
toDecimal("1010") //should return 10.
toDecimal("10010") //should return 18.
toDecimal("1010101") //should return 85.