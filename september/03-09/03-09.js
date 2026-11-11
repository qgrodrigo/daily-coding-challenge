function isPangram(sentence, letters) {

    const allowed = new Set(letters);
    const found = new Set();

    for (const char of sentence.toLowerCase()) {
        if (/[a-z]/.test(char)){
            if (!allowed.has(char)){
                console.log(false);
                return false;
            }
        found.add(char);
        }
    }

    console.log(found.size === allowed.size);
    return found.size === allowed.size;
}

//Tests
isPangram("hello", "hel") //should return false
isPangram("hello", "helow") //should return false
isPangram("hello world", "helowrd") //should return true
isPangram("Hello World!", "helowrd") //should return true
isPangram("Hello World!", "heliowrd") //should return false
isPangram("freeCodeCamp", "frcdmp") //should return false
isPangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz") //should return true