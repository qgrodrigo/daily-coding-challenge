function toBinary(decimal) {

    let binary = '';

    while(decimal > 0){
        binary += decimal % 2;
        decimal = Math.floor(decimal / 2);
    }

    binary = binary.split("").reverse().join("");
    
    console.log(binary);

    return binary;
}

//Tests
toBinary(5) //should return "101".
toBinary(12) //should return "1100".
toBinary(50) //should return "110010".
toBinary(99) //should return "1100011"