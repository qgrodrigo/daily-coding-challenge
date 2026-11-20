function oneHundred(chars) {

    let count = (Math.trunc(100 / chars.length) + 1);
    let sentence = '';

    for (let index = 0; index < count; index++) {
        sentence += chars;
    }

    sentence = sentence.slice(0, 100);

    //console.log(sentence.slice(0, 100).length);

    return sentence;
}

//Tests:
oneHundred("One hundred ") //should return "One hundred One hundred One hundred One hundred One hundred One hundred One hundred One hundred One ".
oneHundred("freeCodeCamp ") //should return "freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeC".
oneHundred("daily challenges ") //should return "daily challenges daily challenges daily challenges daily challenges daily challenges daily challenge".
oneHundred("!") //should return "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!".