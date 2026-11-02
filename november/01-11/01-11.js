function verify(message, key, signature) {

    let messageSum = 0;
    let keySum = 0;
    let isMatched = true

    for(let char of message){
        messageSum += letterValue(char);
    }

    for(let char of key){
        keySum += letterValue(char);
    }

    if(messageSum + keySum != signature){
        isMatched = false; 
    }

    console.log(isMatched);
    return isMatched;
}

function isUpper(letter) {
    return letter === letter.toUpperCase() && letter !== letter.toLowerCase();
}

function isLower(letter) {
    return letter === letter.toLowerCase() && letter !== letter.toUpperCase();
}


function letterValue(letter){

    let value = 0;

    if(isUpper(letter) == true){
        value = letter.charCodeAt(0) - 38;
    }

    if(isLower(letter) == true){
            value = letter.charCodeAt(0) - 96;
    }
    
    return value;
}

// Tests:
verify("foo", "bar", 57) //should return True.
verify("foo", "bar", 54) //should return False.
verify("freeCodeCamp", "Rocks", 238) //should return True.
verify("Is this valid?", "No", 210) //should return False.
verify("Is this valid?", "Yes", 233) //should return True.
verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514) //should return True.