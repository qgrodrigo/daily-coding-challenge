function countWords(sentence) {
    
    let words = sentence.split(" ");
    let count = words.length;
    
    console.log(count);

    return count;
}

//Tests
countWords("Hello world") //should return 2.
countWords("The quick brown fox jumps over the lazy dog.") //should return 9.
countWords("I like coding challenges!") //should return 4.
countWords("Complete the challenge in JavaScript and Python.") //should return 7.
countWords("The missing semi-colon crashed the entire internet.") //should return 7.