function sequence(n) {

    let numbersSequence = '';

    for(let i = 1; i < n + 1; i++){
        numbersSequence += i.toString();
    }

    console.log(numbersSequence);

    return numbersSequence;
}

//Tests:
sequence(5) //should return "12345".
sequence(10) //should return "12345678910".
sequence(1) //should return "1".
sequence(27) //should return "123456789101112131415161718192021222324252627".