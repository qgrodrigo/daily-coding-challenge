function getLongestWord(sentence) {

    sentence = sentence.replace(".", "")
    let words = sentence.split(" ");
    let long_word = words[0];

    for (let index = 1; index < words.length; index++) {
        if(words[index].length > long_word.length){
            long_word = words[index];
        }
    }

    console.log(long_word)

    return long_word;
}

getLongestWord("coding is fun") //should return "coding".
getLongestWord("Coding challenges are fun and educational.") //should return "educational".
getLongestWord("This sentence has multiple long words.") //should return "sentence".